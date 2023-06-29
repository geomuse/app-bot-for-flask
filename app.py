from flask import Flask, request, jsonify , render_template

app = Flask(__name__)

def get_odd_numbers():
    prime_numbers = []
    num = 2
    while len(prime_numbers) < 10:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
        num += 1
    return prime_numbers

def get_even_numbers():
    even_numbers = []
    num = 2
    while len(even_numbers) < 10:
        if num % 2 == 0:
            even_numbers.append(num)
        num += 1
    return even_numbers

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    number = data['number']
    print(type(number))
    number = int(number) 
    print(type(number))
    # result = number * 2
    if number == 1:
        result = get_odd_numbers()
    elif number == 2:
        result = get_even_numbers()
    elif number > 3 :
        result = number * 2
    else :
        result = f'{number} not number.'

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
