from flask import Flask, render_template, request
import random

app = Flask(__name__)

def dahej_calculator(beauty, girl_income, girl_property, 
                     man_income, man_property, education_factor, 
                     drama_index):
    dahej = (
        (1 / (beauty + 1)) * 500000
        + (man_income * 0.3)
        + (man_property * 0.2)
        - (girl_income * 0.25)
        - (girl_property * 0.35)
        + (education_factor * 40000)
        - (drama_index * 100000)
    )

    comments = [
        "Shaadi ke saath free pressure cooker bhi milega!",
        "Dahej negotiation in progress... aunty is sharpening her arguments.",
        "Warning: Groom’s side demanding too much, deploy Chacha-ji ASAP!",
        "Discount offer: Marry now, pay later.",
        "Congratulations! You unlocked ‘Deluxe Wedding Package’ 😂",
        "Dulha ke saath ek free scooter bhi included hai!",
        "Breaking News: Relatives are already calculating your EMI for dahej."
    ]
    
    return max(0, int(dahej)), random.choice(comments)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        beauty = int(request.form['beauty'])
        girl_income = int(request.form['girl_income'])
        girl_property = int(request.form['girl_property'])
        man_income = int(request.form['man_income'])
        man_property = int(request.form['man_property'])
        education_factor = int(request.form['education_factor'])
        drama_index = int(request.form['drama_index'])

        dahej_value, funny_comment = dahej_calculator(
            beauty, girl_income, girl_property,
            man_income, man_property, education_factor,
            drama_index
        )

        return render_template('index.html', dahej_value=dahej_value, funny_comment=funny_comment)

    return render_template('index.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



