flask --app app.py --debug run

Heavy emphasise on using ChatGPT

### **Project Specification: Movie Info Web App (CS50x Final Project)**

#### **Project Overview**

The project will be a web-based application that allows users to search for a movie or show and view detailed information about it. The app will display IMDb ratings, cast, general information, and most importantly, the IMDb Parents Guide section. Additionally, the app will offer embedded trailers, a dynamic light/dark mode switch based on user preferences, and direct links to external materials.

#### **Core Features**

1.  **Search Functionality**:

    -   A search bar to search for movies or shows by title.
    -   Use an API to fetch movie/show data, including IMDb ratings, cast, and additional details.
    -   Ensure the ability to display dynamic, up-to-date movie/show information.
2.  **IMDb Information**:

    -   Display IMDb rating for the selected movie/show.
    -   Show cast and basic details (genre, year, runtime, etc.).
    -   Display the IMDb Parents Guide section, which is crucial for your project.
3.  **Embedded Trailers**:

    -   Embed YouTube or IMDb trailers directly on the page for the selected movie/show.
4.  **Dynamic Theme (Light/Dark Mode)**:

    -   Automatically detect the user's system theme (light/dark mode).
    -   Provide a toggle button for the user to switch between light and dark modes.
5.  **Direct Links**:

    -   Display direct links to the movie/show's IMDb page or other external resources like trailers or reviews.


### **Tech Stack**

-   **Backend**:

    -   Use **Flask** for the backend. Flask is lightweight and easy for beginners. You can scale it later as needed.
    -   Fetch movie/show data from an external API like OMDb (Open Movie Database) to get IMDb ratings and other information.
    -   Store API keys securely (use environment variables or a `.env` file).
-   **Frontend**:

    -   Use **HTML**, **CSS**, and **JavaScript** for the frontend. For more dynamic features like theme switching, you may need JavaScript.
    -   **Bootstrap** or **TailwindCSS** for responsive design (optional but recommended for ease).
    -   The embedded trailers can be fetched from YouTube or IMDb's official trailer links using `<iframe>` tags.
-   **Database**:

    -   Since you mentioned keeping it free and relying on up-to-date information, it's a good idea to **not use a local database**. Instead, fetch data directly from an API like OMDb whenever the user searches for a movie/show.

* * * * *

### **Functional Requirements**

1.  **User Input (Search Bar)**:

    -   The user can enter the title of a movie/show in a search bar.
    -   Upon submitting, the search triggers an API call to retrieve movie/show information.
2.  **Displaying Information**:

    -   **IMDb Rating**: Display the IMDb rating for the selected movie/show.
    -   **Cast**: Display the primary cast (name and role).
    -   **General Info**: Display the genre, release year, and runtime.
    -   **Parents Guide**: Provide a direct link to the IMDb Parents Guide section (using the IMDb ID for the movie/show).
3.  **Embedded Trailers**:

    -   If available, embed a trailer using the IMDb or YouTube video URL (embedded via an iframe).
4.  **Light/Dark Mode**:

    -   The app should detect the system theme (light/dark mode) and adjust the theme accordingly.
    -   Include a toggle button that allows the user to switch themes manually.
    -   Store the user's theme preference in the browser's local storage so that the app remembers the setting.
5.  **External Links**:

    -   Provide external links to:
        -   IMDb page for more information.
        -   Trailer URLs, reviews, or any other relevant materials.

* * * * *

### **Non-Functional Requirements**

1.  **Performance**:

    -   The app should load quickly by fetching movie/show data dynamically.
    -   Minimize reliance on large datasets stored locally; fetch up-to-date information from the API as needed.
2.  **Usability**:

    -   The user interface should be simple and intuitive, with clear navigation and search capabilities.
    -   Design should adapt to both desktop and mobile screen sizes.
3.  **Reliability**:

    -   Use reliable external APIs (like OMDb) to ensure the data fetched is up-to-date and accurate.
    -   Handle errors gracefully if data is not found or an API request fails.

* * * * *

### **Development Milestones**

1.  **Phase 1 - Basic Search and Display**:

    -   Implement search functionality with the Flask backend.
    -   Fetch movie/show data using OMDb API (IMDb ratings, basic details).
    -   Display basic information on the frontend (IMDb rating, cast, genre, etc.).
    -   Add a direct link to the IMDb Parents Guide.
2.  **Phase 2 - Embedding Trailers and Light/Dark Mode**:

    -   Implement embedded trailers for each movie/show (YouTube or IMDb).
    -   Add light/dark mode based on the user's system theme and toggle functionality.
3.  **Phase 3 - Polish and External Links**:

    -   Add more external links like reviews, IMDb page, and trailers.
    -   Test the application on different devices and browsers to ensure it's responsive.