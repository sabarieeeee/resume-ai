from flask import Flask, render_template, request, session, send_file
import os

from parser.text_cleaner import clean_profile_text
from parser.pdf_parser import extract_text_from_pdf
from parser.docx_parser import extract_text_from_docx
from parser.section_extractor import extract_sections
from parser.ats_scorer import score_ats
from parser.resume_generator import generate_resume_content
from parser.ats_builder_scorer import score_builder_resume
from parser.pdf_generator import generate_resume_pdf

app = Flask(__name__)
app.secret_key = "resume_ai_secret_key"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_resume():
    file = request.files.get("resume")

    if not file or file.filename == "":
        return "No file selected"

    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(path)

    if file.filename.lower().endswith(".pdf"):
        text = extract_text_from_pdf(path)
    elif file.filename.lower().endswith(".docx"):
        text = extract_text_from_docx(path)
    else:
        return "Unsupported file format"

    return process_resume(text)


@app.route("/generate", methods=["POST"])
def generate_resume():
    profile_text = request.form.get("profile_text")

    if not profile_text:
        return "No input provided"

    cleaned_text = clean_profile_text(profile_text)
    return process_resume(cleaned_text)


def process_resume(text):
    sections = extract_sections(text)
    original_score, feedback = score_ats(sections)

    generated_resume = generate_resume_content(sections)
    improved_score, _ = score_builder_resume(generated_resume)

    session["generated_resume"] = generated_resume
    session["improved_score"] = improved_score

    return render_template(
        "ats_result.html",
        sections=sections,
        score=original_score,
        feedback=feedback
    )


@app.route("/preview")
def preview():
    resume = session.get("generated_resume")
    improved_score = session.get("improved_score")

    if not resume:
        return "No resume data found"

    return render_template(
        "resume_preview.html",
        generated_resume=resume,
        improved_score=improved_score
    )


@app.route("/download", methods=["POST"])
def download_resume():
    resume = session.get("generated_resume")

    if not resume:
        return "No resume data found"

    filename = request.form.get("filename")
    if not filename:
        return "Invalid file name"

    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, f"{filename}.pdf")

    generate_resume_pdf(resume, output_path)

    return send_file(
        output_path,
        as_attachment=True,
        download_name=f"{filename}.pdf"
    )



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

