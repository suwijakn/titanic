def fake_predict(user_age):
    if user_age > 10:
        prediction = 'survive (>10)'
    else:
        prediction = 'Super survive (<10)'

    return prediction
