from django.shortcuts import render
import random
import datetime
from django.views.decorators.csrf import csrf_exempt
import json
import hashlib
from django.http import JsonResponse

from .models import AppUser

# Create your views here.
sessions = {}


def increment_count(request):
    print(sessions)
    session_id_number = request.COOKIES.get("session_id_number")
    session = sessions.get(session_id_number)

    if not session:
        session_id_number = str(random.randint(100000, 999999))

        sessions[session_id_number] = {
            "count": 1,
            "start_time": datetime.datetime.now(),
        }
    else:
        sessions[session_id_number]["count"] += 1

    response = render(request, "blog/count.html", sessions[session_id_number])
    response.set_cookie("session_id_number", session_id_number)

    return response


def generate_salt():
    return str(random.randint(100000, 999999))


@csrf_exempt
def sign_up(request):
    # the body is a JSON formatted string. let's convert it to a dictionary
    body = json.loads(request.body)
    raw_password = body["password"]

    # a simple helper function that generates a random string
    salt = generate_salt()

    # convert our string to bytes, hash the bytes, then display the hash as hexadecimal
    salted_hashed_password = hashlib.sha256((salt + raw_password).encode()).hexdigest()

    # the salted hash is saved in the database, NOT the plain-text password.
    new_user = AppUser(
        user_name=body["username"], password=f"{salt}${salted_hashed_password}"
    )
    new_user.save()

    # tell the client their request was successful
    return JsonResponse(
        {
            "success": True,
            "salted hashed password": salted_hashed_password,
            "salt": salt,
            "username": body["username"],
        }
    )


@csrf_exempt
def log_in(request):
    # convert the body from a JSON string to a python dictionary
    body = json.loads(request.body)
    # print(body)
    # print(body["username"])
    # print(body["password"])

    # look up the user from the database that this client is claiming to be
    user = AppUser.objects.get(user_name=body["username"])

    # split the 'password' field in the db into its components: the salt and the hash
    split_password = user.password.split("$")
    salt = split_password[0]
    hashed_password = split_password[1]

    # use the salt from the db to hash the password in the request body
    challenge_hash = hashlib.sha256((salt + body["password"]).encode()).hexdigest()
    print(challenge_hash)
    print(hashed_password)
    # if the hashes match, set a cookie to start a session
    if challenge_hash == hashed_password:
        response = JsonResponse({"success": True})
        response.set_cookie("user_id", user.id)
        # print(response)
        return response


def log_in_page(request):
    return render(request, "blog/login.html")
