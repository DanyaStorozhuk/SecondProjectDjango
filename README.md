# 🛠️ Car Repair Service

This is a Django-based web application for people who want to repair their car.
Clients can see which cars we work with, add their own task or describe a problem related to their car, submit a resume (if someone wants to find a job in this field), and users can also leave an honest review about the work of the employees.

---

## 🔧 Features

- **👤 User Authentication:** Viewing cars, submitting a resume, adding a review, and editing your own task.
- **🛠️ Additional Admin Features:** View resumes and hire, add cars, and delete own tasks.
- **📆 Task System:** Authenticated users can add tasks and later delete or edit them.  
- **🚗 Car Cards Browsing:** Users can view our list of cars that we already work with.  
- **📝 Reviews:** Users can leave feedback about the servicing of their car.  
- **📄 Resume Submission:** Users who want to find a job can send their resume to the administrator.  
- **🔍 Filtering:** Users can filter reviews by date and tasks by status.  
- **👥 Employee Overview:** Users can view the employees working in our service.  
---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** HTML/СSS/JS (Django templates) 
- **Authentication:** Django built-in auth system with custom user model
---

## 🚀 Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/DanyaStorozhuk/SecondProjectDjango.git
    cd Django_myProject_logika
    ```

2. **Set Up a Virtual Environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    Install Dependencies:
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser (Optional)**:

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:

    ```bash
    python manage.py runserver
    ```


Access the application at http://127.0.0.1:8000

# Task & Resume Management System

## Project Structure

- `tasks/`: Main app containing models, views, forms, and templates for tasks, resumes, comments, and cars.  
- `users/` (optional): Can contain the custom user model and forms for registration and login.  
- `templates/tasks/`: HTML templates for lists, forms, and detail views of models.  

## Templates

- `task_list.html`: Task list with status filtering.  
- `task_detail.html`: Task detail page.  
- `task_form.html`: Form to create a new task.  
- `task_update_form.html`: Form to update an existing task.  
- `task_delete_confirmation.html`: Task deletion confirmation page.  
- `task_comment.html`: Form to create a comment.  
- `worker_task_detail.html`: List of approved resumes.  
- `new_resume.html`: List of new resumes.  
- `task_resume.html`: Form to create a resume.  
- `add_auto.html`: Form to add a car.  
- `task_auto.html`: List of user cars.  

## Models

- **CustomUser**: Extends `AbstractUser` with additional fields (`phone`, `passport`, `role`).  
- **Task**: Task model with `title`, `description`, `status`, `priority`, `due_date`, and `creator`.  
- **Comment**: Comments related to tasks with `author` and creation date.  
- **Resume**: User resume with `title`, `experience`, `education`, `skills`, and `status`.  
- **Car**: User cars with `brand`, `model`, `year`, `owner`, and `photo`.  

## URL Structure

- `/` — Home page.  
- `/register/` — User registration.  
- `/login/` — User login.  
- `/task/` — List of tasks.  
- `/task-create/` — Create a new task.  
- `/<int:pk>/` — Task detail view.  
- `/<int:pk>/update/` — Edit a task.  
- `/<int:pk>/delete/` — Delete a task.  
- `/task-comment/` — Add a comment.  
- `/worker-task-detail` — List of approved resumes.  
- `/new-resume` — List of new resumes.  
- `/task-resume` — Create a new resume.  
- `/resume/<int:pk>/approve/` — Approve a resume.  
- `/resume/<int:pk>/reject/` — Reject a resume.  
- `/add-auto` — Add a car.  
- `/task-auto` — List of cars.  
- `/<int:pk>/complete/` — Mark task as "done".  

## Usage

- **Register or Log In**: Create an account or log in to access tasks, resumes, and cars.  
- **View Tasks**: Browse tasks and filter them by status.  
- **Manage Tasks**: Create, update, delete tasks, and mark tasks as completed.  
- **Add Comments**: Post comments for tasks.  
- **Manage Resumes**: Create resumes, view new resumes, approve or reject them.  
- **Manage Cars**: Add cars and view the list of user cars.

## Future Improvements
- Expand functionality
- Make the code more readable
- Add filtering by cars
- Allow users to choose the mechanic they liked before
- Enable rating the worker
- Create a ranking of cars that visit the station most frequently