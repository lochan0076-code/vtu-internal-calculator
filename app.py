from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>VTU Internal Marks Calculator</title>
</head>
<body>
    <h2>VTU Internal Marks Calculator</h2>
    <p>Enter marks as per VTU guidelines</p>

    <form method="post">
        CIE 1 (out of 20):
        <input type="number" name="cie1" min="0" max="20" required><br><br>

        CIE 2 (out of 20):
        <input type="number" name="cie2" min="0" max="20" required><br><br>

        Assignment / Quiz (out of 10):
        <input type="number" name="assignment" min="0" max="10" required><br><br>

        <button type="submit">Calculate Internal Marks</button>
    </form>

    {% if result is not none %}
        <h3>Best CIE: {{ best_cie }}/20</h3>
        <h3>Total Internal Marks: {{ result }}/30</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    best_cie = None

    if request.method == "POST":
        cie1 = int(request.form["cie1"])
        cie2 = int(request.form["cie2"])
        assignment = int(request.form["assignment"])

        best_cie = max(cie1, cie2)
        result = best_cie + assignment

    return render_template_string(
        HTML,
        result=result,
        best_cie=best_cie
    )

if __name__ == "__main__":
    app.run(debug=False)
