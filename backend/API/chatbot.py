import os
import json
from flask import Blueprint, request, jsonify

chatbot_bp = Blueprint('chatbot', __name__)
json_path = os.path.join(os.path.dirname(__file__), "personalapi.json")
with open(json_path) as f:
    data = json.load(f)

#----------------------------------------------------------------------------#
def get_response(message: str):
    msg = message.lower()

    if "cert" in msg or "certifications" in msg:
        certs = data.get("Certifications", [])
        if not certs:
            return "No certifications found."
        return "Here are my certifications:\n" + "\n".join(
            f"⭐⭐ {c['name']} ({c['issuer']}, {c['issued_on']}) ⭐⭐" for c in certs
        )

    if "about" in msg or "who are you" in msg or "about me" in msg:
        about = data.get("AboutMe", {})
        return (
            f"My name is {about.get('name', 'Andres')}. "
            f"I am a {about.get('title', 'professional')}. "
            f"My goals: {about.get('goals', '')} "
        )

    if "skills" in msg:
        skills = data.get("Skills", {})
        tech = ', '.join(skills.get("Technical", []))
        sec = ', '.join(skills.get("Security & Infrastructure", []))
        return f"My technical skills include: {tech}\nSecurity and infrastructure skills: {sec}"

    if "projects" in msg:
        projects = data.get("Projects", [])
        if not projects:
            return "No projects found."
        return "Here are some projects I've worked on:\n" + "\n".join(
            f"- {p['name']}: {p['description']}" for p in projects
        )

    return "Sorry, I can only answer questions about Andres Jaimes’ career, work, or background."

#---------------------------------------------------------------------------------#
@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    data_in = request.get_json()
    print(f"Received message: {data_in.get('message')}")
    response = get_response(data_in.get('message', ''))
    print(f"Sending response: {response}")
    return jsonify({"response": response})