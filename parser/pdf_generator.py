from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import black, grey


def generate_resume_pdf(resume, file_path):
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    left = 1 * inch
    right = width - 1 * inch
    y = height - 1 * inch

    # ---------- NAME ----------
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(black)
    c.drawString(left, y, resume["Name"])
    y -= 30

    # ---------- CONTACT ----------
    c.setFont("Helvetica", 10)
    c.setFillColor(grey)
    c.drawString(left, y, f'{resume["Email"]} | {resume["Phone"]}')
    y -= 28

    # ---------- PROFILE SUMMARY ----------
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(black)
    c.drawString(left, y, "PROFESSIONAL SUMMARY")
    y -= 6
    c.line(left, y, right, y)
    y -= 14

    c.setFont("Helvetica", 11)
    summary = (
        "Motivated Computer Science graduate with a strong foundation in "
        "software development, problem-solving, and modern programming "
        "technologies. Seeking an entry-level role to apply technical skills "
        "and contribute to impactful projects."
    )
    text_obj = c.beginText(left, y)
    text_obj.textLines(summary)
    c.drawText(text_obj)
    y -= 40

    # ---------- SECTION HELPER ----------
    def section(title):
        nonlocal y
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(black)
        c.drawString(left, y, title.upper())
        y -= 6
        c.line(left, y, right, y)
        y -= 14
        c.setFont("Helvetica", 11)

    # ---------- BULLET HELPER ----------
    def bullet(text):
        nonlocal y
        c.drawString(left + 10, y, u"\u2022")
        c.drawString(left + 22, y, text)
        y -= 16

    # ---------- SKILLS ----------
    section("Skills")
    c.drawString(left, y, resume["Skills"])
    y -= 26

    # ---------- EDUCATION ----------
    section("Education")
    c.drawString(left, y, resume["Education"])
    y -= 26

    # ---------- PROJECTS ----------
    section("Projects")
    for p in resume["Projects"]:
        bullet(p)
    y -= 10

    # ---------- EXPERIENCE ----------
    section("Experience")
    for e in resume["Experience"]:
        bullet(e)

    c.save()
