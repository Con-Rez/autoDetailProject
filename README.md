# AK Auto Detail Website

![Logo](https://github.com/Con-Rez/autoDetailProject/blob/main/apps/home/static/imgs/logo.jpg?raw=true)

## Project Overview

AK Auto Detail, provides comprehensive auto detailing services to both private dealerships and the public. Despite offering high-quality services such as interior cleaning, exterior polishing, engine detailing, and headlight restoration. 

This project's goal was to provide an appealing, functional, and user-friendly website for AK Auto Detail to allow customers to book appointments, estimate costs, and view examples of previous customers' vehicles. 

## Features

- Visually appealing homepage with a light and dark mode
- Platform to highlight positive customer reviews
- Highlights Instagram feed
- Dedicated Photo Gallery, showcasing Before-And-After images and Videos
- A Services Calculator to allow customers to estimate cost and time before booking
- Integrated appointment scheduler, synced with Google Calendar integration
- Optimized for mobile, tablet, and desktop users

---

## Authors

- [@Con-Rez](https://github.com/Con-Rez) Connor Puckett. Contact: cpuckett@csus.edu
- [@RebeccaFitzpatrick](https://github.com/RebeccaFitzpatrick) Rebecca Fitzpatrick. Contact: rebeccafitzpatrick@csus.edu.
- [@Rodrigo-Guzman3](https://github.com/Rodrigo-Guzman3) Rodrigo Guzman. Contact: Rodrigoguzman@csus.edu
- [@fanbrandon](https://github.com/fanbrandon) Brandon Fan. Contact: bfan@csus.edu
- [@Serefima](https://github.com/Serefima) Odalis Torres. Contact: otorres@csus.edu
- [@katerinacowan](https://github.com/katerinacowan) Katerina Cowan. Contact: katerinacowan@csus.edu
- [@Pencilsharp333](https://github.com/Pencilsharp333) Matthew Pabon. Contact: matthewpabon3@csus.edu
- [@un90](https://github.com/un90) Uzma Naz. Contact: uzmanaz@csus.edu
- [@tonymai9](https://github.com/tonymai9) Tony Mai. Contact: tonymai@csus.edu

---

## Deployment

This project assumes you have downloaded and installed the following on your Linux server.

- [Python](https://www.python.org/downloads/)
- [PIP](https://pip.pypa.io/en/stable/installation/)

Then, use the `git clone` command to copy the project files over.

```bash
git clone https://github.com/Con-Rez/autoDetailProject.git
```

To deploy this project, first install the PIP dependencies listed in the included requirements.txt

```bash
pip install -r requirements.txt
```

Before running any tests, make sure to install Selenium
```bash
pip install selenium webdriver-manager
```

Then run the server
```bash
python manage.py runserver
```

---

## Running Tests

To run tests, you can use the following commands.

```bash
# Run all tests in the 'home' package
$ python manage.py test home

# Run all the tests in the 'home' app
$ python manage.py test home.tests

# Run just one test case class (example: Appointment tests)
$ python manage.py test home.tests.test_appointment.AppointmentTests

# Run just one test method (example: test_create_appointment from the AppointmentTests class)
$ python manage.py test home.tests.test_appointment.AppointmentTests.test_create_appointment

```
More info can be found here: [Django Testing Documentation](https://docs.djangoproject.com/en/5.1/topics/testing/overview/)


---

## Documentation

Additional information and developer resources are available in the [Project Wiki](https://github.com/Con-Rez/autoDetailProject/wiki).

---

## Screenshots

### Home Page
![homeScreenshot](https://github.com/Con-Rez/autoDetailProject/blob/main/docs/images/homeScreenshotv2Long.png?raw=true)

### About Us
![aboutUsScreenshot](https://github.com/Con-Rez/autoDetailProject/blob/main/docs/images/aboutUsScreenshot.png?raw=true)

### Gallery
![galleryScreenshot](https://github.com/Con-Rez/autoDetailProject/blob/main/docs/images/galleryScreenshot.png?raw=true)

### Schedule Appointment
![appointmentsScreenshot](https://github.com/Con-Rez/autoDetailProject/blob/main/docs/images/appointmentsScreenshot.png?raw=true)

### Contact Us
![contactUsScreenshot](https://github.com/user-attachments/assets/5c6c7c44-42e3-49a7-bd30-9f4a0f8e2971)
