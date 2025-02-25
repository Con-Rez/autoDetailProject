
![Logo](https://github.com/Con-Rez/autoDetailProject/blob/main/apps/home/static/imgs/logo.jpg?raw=true)


# AK Auto Detail Website

AK Auto Detail, provides comprehensive auto detailing services to both private dealerships and the public. Despite offering high-quality services such as interior cleaning, exterior polishing, engine detailing, and headlight restoration. This project provides a user-friendly website for AK Auto Detail. 






## Features

- Platform to highlight positive customer reviews
- Visually Appealing Home Page
- Highlights Instagram Feed
- Dedicated Photo Gallery, showcaseing Before-And-After images
- Integrated appointment scheduler, synced with Google Calendar integration
- A Light and Dark Mode


## Authors

- [@Con-Rez](https://github.com/Con-Rez)
- [@RebeccaFitzpatrick](https://github.com/RebeccaFitzpatrick)
- [@Rodrigo-Guzman3](https://github.com/Rodrigo-Guzman3)
- [@fanbrandon](https://github.com/fanbrandon)
- [@Serefima](https://github.com/Serefima)
- [@katerinacowan](https://github.com/katerinacowan)
- [@Pencilsharp333](https://github.com/Pencilsharp333)
- [@un90](https://github.com/un90)
- [@tonymai9](https://github.com/tonymai9)

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

then run the following for test_(insert name thats appropiate for your task).py to work (you'll need to create new test_(name).py files for your new tasks you want to test, create it in the same folder as test_dismodal.py and tests.py)
```bash
pip install selenium webdriver-manager
```

Then run the server.

```bash
python manage.py runserver
```

to run the test files using selenium:
```bash
python manage.py test home
```

## Running Tests

To run tests, you can use the following commands. More info can be found here: [Django Testing Documentation](https://docs.djangoproject.com/en/5.1/topics/testing/overview/)

```bash
# Run all the tests in the animals.tests module
$ ./manage.py test animals.tests

# Run all the tests found within the 'animals' package
$ ./manage.py test animals

# Run just one test case class
$ ./manage.py test animals.tests.AnimalTestCase

# Run just one test method
$ ./manage.py test animals.tests.AnimalTestCase.test_animals_can_speak
```


## Documentation

We have a Project Wiki containing the documentation regarding managing the code and project into the future: [Project Wiki](https://github.com/Con-Rez/autoDetailProject/wiki)


## Roadmap

Further planned development information can be found via...
- [The Figma Prototype](https://www.figma.com/design/n5vPLWYCKmbhHrYgbkFscb/Detail-shop-mockup?node-id=0-1&t=g3LebtGtZ8f6anEN-1)
- [The Jira Board](https://zeros-and-ones.atlassian.net/jira/software/projects/SCRUM/boards/1)

### Sprint 5 (Week 1-2)
**Focus:** Refining and expanding core features while preparing the server for deployment.  
**Milestones:**
- **Enhancements:** Improve and finalize the header, banner, and footer sections (part 2).
- Expand on "Our Services," "Our Transformation," "Who We Are," and "Google Reviews" pages.
- Add additional functionality to social media integration.  
**Additional Objectives:**
- Implement a login portal for photo management.
- Set up and configure the hosting server.

---

### Sprint 6 (Week 3-4)
**Focus:** Iterative refinement and debugging of core features.  
**Milestones:**
- **Enhancements:** Further refine and finalize "Choose a Date" and "Pick a Time" scheduling functionalities (part 2).
- Improve the customer contact/communication interface.  
**Additional Objectives:**
- Conduct comprehensive code cleanup and restructuring.
- Begin extensive debugging and testing.
- Document and address external dependencies to ensure long-term stability.

---

### Sprint 7 (Week 5-6)
**Focus:** Comprehensive documentation and gallery refinements.  
**Milestones:**
- **Enhancements:** Polish and expand the "Before/After" transformation showcase (part 2).
- Apply final improvements to the transformation gallery and user flows.  
**Additional Objectives:**
- Develop in-depth GitHub Wiki documentation for maintaining the website.
- Include guides on photo management, the appointments calendar, and troubleshooting for internal use.

---

### Sprint 8 (Week 7-8)
**Focus:** Final testing, deployment, and wrapping up documentation.  
**Milestones:**
- **Enhancements:** Finalize all remaining UI/UX adjustments, including home view, scheduling system, and gallery features (part 2).
- Complete final testing and debugging for a production-ready site.  
**Additional Objectives:**
- Wrap up documentation on GitHub Wiki.
- Prepare for live deployment and ensure all features are stable.

---

## Screenshots

![App Screenshot](https://github.com/Con-Rez/autoDetailProject/blob/main/websitePreviewExample.png?raw=true)

