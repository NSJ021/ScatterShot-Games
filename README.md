# ScatterShot Games

<p align="center">
<img src=".\ReadMe_Images\ssg_final_product.png" alt="ssg final product image">
</P>
<br>

## Overview

### Purpose

<p align="center">
<img src=".\ReadMe_Images\ssg_logo.jpg" alt="ssg logo">
</P>
<br>

ScatterShot Games, is an Indie Board Games Creator. With already 4+ custom board games created in house and available to purchase.
The purpose of this project is to create a full stack web application to allow ScatterShot to gain some online presence
and build the brand as well as the business in general.

The web application created as part of this project, will showcase Games, News/Blog articles and general information about ScatterShot and their business.

### Target Audience

With regards to a target audience, ScatterShot already has a following within the board game enthusiast space.
There is no official target audience for this project other than to promote this growing Indie business and the great products they create.

## User Stories

### Must-Have User Stories

-   **User Story 1:** Briefly describe the must-have feature.  
    **Acceptance Criteria:** List the criteria that define the successful implementation of this user story.
-   **User Story 2:** Briefly describe the must-have feature.  
    **Acceptance Criteria:** List the criteria that define the successful implementation of this user story.

(Include all prioritized must-have features)  
**Guidance:** Draft the user stories during Phase 1: Ideation & Initial Setup and update them as you complete Phase 2: Must User Stories Implementation & Testing. Document each must-have feature here along with its acceptance criteria.

### Should-Have User Stories

-   **User Story 1:** Briefly describe the should-have feature.  
    **Acceptance Criteria:** List the criteria that define the successful implementation of this user story.
-   **User Story 2:** Briefly describe the should-have feature.  
    **Acceptance Criteria:** List the criteria that define the successful implementation of this user story.

(Include all prioritized should-have features)  
**Guidance:** Document the secondary features that you aim to implement in Phase 3: Should User Stories Implementation & Any Advanced Features. Include clear acceptance criteria for each.

### Could-Have User Stories

-   **User Story 1:** Briefly describe the could-have feature.  
    **Acceptance Criteria:** List the criteria that define the successful implementation of this user story.
-   **User Story 2:** Briefly describe the could-have feature.  
    **Acceptance Criteria:** List the criteria that define the successful implementation of this user story.

(Include any could-have features considered for future enhancements)  
**Guidance:** Document any optional features that are nice to have but not essential.

## Design Decisions

### Project Board

To keep the project on track, manage scope and work to Agile methodology a kanban style project board was created.
This project board is continuously updated and utilised throughout the development cycles of the project.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_projectboard_1.png" alt="ssg project board image">
</P>
<br>

<p align="center">
<img src=".\ReadMe_Images\ssg_projectboard_2.png" alt="ssg project board image">
</P>
<br>

### Entity Relationship Diagram

The diagram linked below shows the relationship between all the tables / Models used throughout the project.
The user, once authenticated is referenced at various points in other models.
Each user can comment on a game and blog post, they will ahve control over editing and deleting their own commeents also.
However, no comment will be made Live until an Admin user has approved the comment.
This functionality highlights the <strong>CRUD</strong> abilities within the project.

A brief description of the relationships are as follows:

User from User Model is always a 1 to 1 relationship.
Every Game can have many comments, but a comment can only belong to a single game
Every Blog Post can have many comments, but a comment can only belong to a single post.
A User can send many messages, but a message can only belong to one user.
The team model is not linked to any other model via a relationship, as this functionality was not required for this project.

<p align="center">
<img src=".\ReadMe_Images\Entity_relationship_diagram.png" alt="ssg project board image">
</P>
<br>

### Wireframes

Include wireframes for key sections of your website.  
Briefly describe the design choices, including layout, colour schemes, and fonts.  
**Guidance:** Start this section during Phase 1: Ideation & Initial Setup and update it throughout Phase 2 and Phase 3. Include digital wireframes created in Phase 1. Document the reasoning behind your layout choices, colour schemes, and font selections.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_wireframe_desktop.png" alt="ssg wireframe desktop image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_wireframe_tablet.png" alt="ssg wireframe tablet image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_wireframe_mobile.png" alt="ssg wireframe mobile image">
</P>
<br>

### Accessibility Considerations

#### Colour Scheme

The chosen colour scheme, compliments the themes used within Scattershots products as well as pleasing to the eye.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_colour_scheme.png" alt="ssg colour scheme image">
</P>
<br>

#### Colour Contrast

Colour contrast was considered during the colour scheme selection. Details are shown below.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_colour_contrast.png" alt="ssg colour contrast image">
</P>
<br>

#### Fonts

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_font_1.png" alt="ssg font image">
</P>
<br>

#### LightHouse Scores

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_lighthouse_1.png" alt="ssg lighthouse score image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_lighthose_2.png" alt="ssg lighthouse score image">
</P>
<br>

Discuss how accessibility guidelines were adhered to, including colour contrast and alt text for images.  
**Guidance:** Outline how you've incorporated accessibility into your design, ensuring that your project adheres to guidelines such as WCAG.

## Features Implementation

### Core Features (Must-Haves)

-   **Feature 1:** Description of the implemented feature.
<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_1.png" alt="ssg feature image">
</P>
<br>

-   **Feature 2:** Description of the implemented feature.
<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_2.png" alt="ssg feature image">
</P>
<br>

(Include all must-have features)  
**Guidance:** Use this section as you complete Phase 2: Must User Stories Implementation & Testing. Document all the must-have features you implemented, explaining how they align with the user stories and acceptance criteria.

### Advanced Features (Should-Haves)

-   **Feature 1:** Description of the implemented feature.
<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_3.png" alt="ssg feature image">
</P>
<br>

-   **Feature 2:** Description of the implemented feature.
<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_4.png" alt="ssg feature image">
</P>
<br>

(Include all should-have features)  
**Guidance:** Include any advanced features you implemented during Phase 3: Should User Stories Implementation & Any Advanced Features. Explain how these features enhance user experience and their alignment with the acceptance criteria.

### Optional Features (Could-Haves)

-   **Feature 1:** Description of the implemented feature (if any).
<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_5.png" alt="ssg feature image">
</P>
<br>

-   **Feature 2:** Description of the implemented feature (if any).
<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_6.png" alt="ssg feature image">
</P>
<br>

(Include any could-have features that were implemented or considered)  
**Guidance:** If any could-have features were implemented, describe them here. This is an opportunity to showcase extra work done beyond the initial scope. But remember - keep it simple! Focus on the Must stories first. Could user story features are commonly earmarked for future project iterations.

## Testing and Validation

### Testing Results

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_testing_1.png" alt="ssg testing image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_testing_2.png" alt="ssg testing image">
</P>
<br>

Summarize the results of testing across different devices and screen sizes.  
Mention any issues found and how they were resolved.  
**Guidance:** Summarize the results of your testing across various devices using tools like Chrome DevTools, as outlined in Phase 2. Mention any issues found and how they were resolved.

### Validation

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_html_validator.png" alt="ssg html validator image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_css_validator.png" alt="ssg css validator image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_JS_linter.png" alt="ssg JS linter image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_python_linter.png" alt="ssg python linter image">
</P>
<br>

Discuss the validation process for HTML and CSS using W3C and Jigsaw validators.  
Include the results of the validation process.  
**Guidance:** Document your use of W3C and Jigsaw validators to ensure your HTML and CSS meet web standards. Include any errors or warnings encountered and how they were resolved.

## AI Tools Usage

### GitHub Copilot

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_copilot_1.png" alt="ssg copilot image">
</P>
<br>

Brief reflection on the effectiveness of using AI tools for debugging and validation.  
**Guidance:** Reflect on how GitHub Copilot assisted with debugging and validation, particularly any issues it helped resolve.

## Deployment

### Deployment Process

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_heroku_1.png" alt="ssg heroku deployment image">
</P>
<br>

Briefly describe the deployment process to GitHub Pages or another cloud platform.  
Mention any specific challenges encountered during deployment.  
**Guidance:** Describe the steps you took to deploy your website during Phase 4: Final Testing, Debugging & Deployment, including any challenges encountered.

## Code Attribution and Credit

### Jquery, Gallery, SlickSlide etc

To create a more polished and interactive experience I utilised various javascript scripts to create the image galleries, magnification effect, and scroll-up functionality.

**Sources** <br> <br>
[Slick.js](http://kenwheeler.github.io) <br> Slick provides a smooth side scroll function for the website<br>
[Light Gallery](http://sachinchoolur.github.io/lightGallery/) <br> Light Gallery, alongside Magnific Pop Up provides a great looking image gallery utilised across the site<br>
[Jquery Magnific Popup](http://dimsemenov.com/plugins/magnific-popup/) <br> Magnific provides an interactive image zoom and pop up functionality which works alongside the gallery.<br>
[Jquery](https://www.jqueryscript.net/) <br> Core Jquery code to allow jquery plugins to work properly<br>
[Scroll Up](https://markgoodyear.com/2013/01/scrollup-jquery-plugin/) <br> Scroll Up is another Jquery plugin that allows the user to jump back to the top of the page<br>
[Bootstrap](https://getbootstrap.com) <br> Bootstrap used for responsiveness, styling and required for the above plugins and functionality<br>

## Reflection on Development Process

### Successes

Effective use of AI tools, including GitHub Copilot, and how they contributed to the development process.

### Challenges

Describe any challenges faced when integrating AI-generated content and how they were addressed.

### Final Thoughts

Provide any additional insights gained during the project and thoughts on the overall process.  
**Guidance:** Begin drafting reflections during Phase 1 and update throughout the project. Finalize this section after Phase 4. Highlight successes and challenges, particularly regarding the use of AI tools, and provide overall insights into the project.

## Future Improvements

Briefly discuss potential future improvements or features that could be added to the project.  
**Guidance:** Reflect on potential enhancements that could be made to the project after Phase 4: Final Testing, Debugging & Deployment. These could be Could user story features you didn’t have time to implement or improvements based on testing feedback.
