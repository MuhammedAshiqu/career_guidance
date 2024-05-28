# Career Guidance System

This project is a Career Guidance System designed to help users evaluate their skills and interests to suggest potential job roles that align with their capabilities.

## Description

The system consists of three main HTML files:

1. **index.html**: Landing page for the Career Guidance System. Users can start the assessment from this page.
2. **input.html**: Assessment form where users can evaluate themselves based on various skills and competencies.
3. **output.html**: Result page that displays the suggested job role based on the user's assessment.

## Usage

To use the system, follow these steps:

1. Navigate to the landing page by accessing the `index.html`.
2. Click on the "Get Started!" button to begin the assessment.
3. Fill out the assessment form on the `input.html` page by selecting the appropriate skill levels for each category.
4. Submit the form to view the suggested job role on the `output.html` page.

## Technologies Used

- **Django**: Django is used as the web framework for the project.
- **Joblib**: Joblib is used to load the machine learning model for predicting job roles based on user assessments.

## File Structure

- **views.py**: Contains the Django views responsible for rendering HTML templates and processing form submissions.
- **model/**: Directory containing the machine learning model used for job role prediction.
- **static/css/**: Directory containing CSS stylesheets for the HTML templates.

## Setup

To run the project locally:

1. Install Python and Django on your system.
2. Clone this repository.
3. Navigate to the project directory.
4. Install the required dependencies using `pip install -r requirements.txt`.
5. Run the Django server using `python manage.py runserver`.
6. Access the Career Guidance System through your web browser at `http://localhost:8000`.

##Output
![1](https://github.com/MuhammedAshiqu/career_guidance/assets/69718823/09affdb5-aa8c-4583-98e0-3ead63d77503)
![2](https://github.com/MuhammedAshiqu/career_guidance/assets/69718823/1e8d3307-e06b-4cd3-88eb-7d28df0c4672)
![3](https://github.com/MuhammedAshiqu/career_guidance/assets/69718823/1697bfa0-4f17-4ba9-8744-1d1799d32853)
![4](https://github.com/MuhammedAshiqu/career_guidance/assets/69718823/f92f70ad-e1c5-4230-bb28-6c574a7c6d6f)
![5](https://github.com/MuhammedAshiqu/career_guidance/assets/69718823/c2a14b46-0b27-4238-8119-02398d4bf360)

