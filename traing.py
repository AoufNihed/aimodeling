"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from pathlib import Path
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

model = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Validate that an image is present
if not (img := Path("image0.jpeg")).exists():
  raise FileNotFoundError(f"Could not find image: {img}")

image_parts = [
  {
    "mime_type": "image/jpeg",
    "data": Path("image0.jpeg").read_bytes()
  },
]

prompt_parts = [
  "i have post in linkedin and i want to matching between cv and the post with skills and feauters and give a pourcantege about matching:\nthe post is:\nAbout the job\nLOCATION: Remote Work\n\nSCHEDULE: Part-time\n\nAre you a budding frontend developer seeking an exceptional opportunity to gain hands-on experience while working with a prestigious Management Consulting firm? TalentKompass Deutschland, a leading Human Resources company based in Germany, is searching for a highly motivated Frontend Development Intern to join our esteemed client. This remote position offers a unique chance for someone passionate about web development and eager to learn in a dynamic and fast-paced environment.\n\nAs a Frontend Development Intern, you will work closely with the development and consulting teams, where you will be responsible for a range of tasks, including coding, debugging, and collaborating on innovative web solutions. You will have the extraordinary opportunity to learn from experienced professionals who will provide mentorship and guidance throughout the internship. With this internship, you will gain valuable experience in frontend development, web design, and teamwork - all essential skills for a successful career in this field.\n\nResponsibilities:\n\nAssist in the development, testing, and maintenance of web applications using HTML, CSS, and JavaScript\nCollaborate with cross-functional teams to gather requirements and design user interfaces\nDebug and troubleshoot frontend issues, ensuring optimal performance and user experience\nImplement responsive web design principles to ensure applications render well on various devices and screen sizes\nAdhere to coding best practices and maintain code quality\nParticipate in code reviews and contribute to the improvement of development processes\nSupport the team with general administrative tasks as needed\n\n\nRequirements:\n\nBasic understanding of web development principles and practices\nFamiliarity with HTML, CSS, and JavaScript\nExcellent written and verbal communication skills in English\nAbility to work independently and as part of a team\nStrong organizational skills and the ability to manage multiple projects simultaneously\nKnowledge of modern web development tools and frameworks, such as React or Angular, is a plus\nExperience with version control systems, such as Git, is a plus\n\n\nAt TalentKompass Deutschland, we are committed to helping our interns develop their skills and reach their full potential. Our client is a reputable Management Consulting firm that will provide invaluable experience in a competitive industry. Don't miss this fantastic opportunity to jump-start your career in frontend development - apply now!\n\nthe cv is :\n\nCertainly! Here's a simplified example of a computer science CV:\n[Your Name]\n[Your Address]\n[City, State, ZIP Code]\n[Your Email Address]\n[Your Phone Number]\n[LinkedIn Profile]\n[GitHub Profile]\nObjective:\nMotivated computer science graduate with a strong foundation in programming and problem-solving. Seeking a challenging position to apply technical skills in a dynamic and collaborative environment.\nEducation:\nBachelor of Science in Computer Science\n[University Name, City, State]\nGraduation Date: [Month Year]\nRelevant Courses:\nData Structures and Algorithms\nDatabase Management Systems\nWeb Development with HTML, CSS, and JavaScript\nSkills:\nProgramming Languages: Java, Python, C++\nWeb Development: HTML, CSS, JavaScript\nDatabase Management: MySQL\nTools: Git, Jira\nOperating Systems: Windows, Linux\nProblem-Solving\nTeam Collaboration\nProjects:\nOnline Bookstore System\nDeveloped a web-based bookstore system using Java and MySQL.\nImplemented user authentication, order processing, and inventory management.\n[Link to Project on GitHub]\nPersonal Portfolio Website\nCreated a responsive portfolio website using HTML, CSS, and JavaScript.\nShowcased projects, skills, and contact information.\n[Link to Project]\nWork Experience:\nIntern, Software Development - XYZ Company, City, State\nMonth Year - Month Year\nAssisted in the development of a customer relationship management (CRM) system.\nCollaborated with the team to troubleshoot and debug software issues.\nContributed to the design and implementation of new features.\nInternships:\nSoftware Engineering Intern - ABC Tech, City, State\nMonth Year - Month Year\nWorked on a team project to enhance the functionality of an e-commerce platform.\nConducted code reviews and collaborated with team members to optimize code.\nCertifications:\nJava Programming Certification - Oracle, [Date]\nAwards:\nOutstanding Student in Computer Science - [University Name], [Year]\nLanguages:\nEnglish (Fluent)\nReferences:\nAvailable upon request.\n\n\n",
  image_parts[0],
]

response = model.generate_content(prompt_parts)
print(response.text)