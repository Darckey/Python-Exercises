def assert_if_input_is_numeric(input):
    try:
        value = int(input)
        print(f'Correct, you gave numeric valua => {value}')
    except ValueError:
        try:
            value = float(input)
            print(f'Correct, you gave numeric valua with decimals => {value}')
        except ValueError:
            print(f'Enterad value "{input}" is not numeric')

user_input = input("Enter numeric value! ")
assert_if_input_is_numeric(user_input)