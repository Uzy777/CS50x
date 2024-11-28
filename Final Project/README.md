# Movie Info Web App (CS50x Final Project)

## Project Overview

The Movie Info Web App allows users to search for a movie or show and view detailed information about it. The app provides IMDb ratings, cast information, general movie/show details, embedded trailers, and the IMDb Parents Guide section. Additionally, users can switch between light and dark modes based on their system preferences, with a toggle button for manual switching. External links to IMDb pages and other resources are also provided.

## Core Features

### 1. Search Functionality:
- A search bar to search for movies or shows by title.
- Fetch data from an API to display movie/show information, including IMDb ratings, cast, and additional details.
- Display up-to-date movie/show information dynamically.

### 2. IMDb Information:
- Show IMDb rating for the selected movie/show.
- Display cast and basic details (genre, year, runtime, etc.).
- Include a direct link to the IMDb Parents Guide section, which is essential for the project.

### 3. Embedded Trailers:
- Embed YouTube or IMDb trailers directly on the page for the selected movie/show.

### 4. Dynamic Theme (Light/Dark Mode):
- Automatically detect the user’s system theme (light/dark mode).
- Provide a toggle button for users to manually switch between light and dark modes.

### 5. External Links:
- Display direct links to the IMDb page or other external resources like trailers or reviews.

---

## Tech Stack

### Backend:
- **Flask** for the backend. It is lightweight and beginner-friendly.
- Fetch movie/show data from an external API (like OMDb or TMDb) to get IMDb ratings and other information.
- Store API keys securely (use environment variables or a `.env` file).

### Frontend:
- **HTML**, **CSS**, **JavaScript** for the frontend.
- **Bootstrap** or **TailwindCSS** for responsive design (optional but recommended for ease).
- Embedded trailers can be fetched from YouTube or IMDb’s official trailer links using `<iframe>` tags.

### Database:
- No local database used. Data is fetched directly from the API to ensure up-to-date information.

---

## Functional Requirements

### 1. User Input (Search Bar):
- Users can enter the title of a movie/show in the search bar.
- Upon submitting, an API call is triggered to retrieve movie/show information.

### 2. Displaying Information:
- **IMDb Rating**: Display the IMDb rating for the selected movie/show.
- **Cast**: Display the primary cast (name and role).
- **General Info**: Display the genre, release year, and runtime.
- **Parents Guide**: Provide a direct link to the IMDb Parents Guide section using the IMDb ID.

### 3. Embedded Trailers:
- If available, embed a trailer using the IMDb or YouTube video URL (embedded via an iframe).

### 4. Light/Dark Mode:
- The app automatically detects the system theme (light/dark mode) and adjusts the theme accordingly.
- Include a toggle button for users to manually switch themes.
- Store the user’s theme preference in the browser's local storage.

### 5. External Links:
- Provide external links to:
  - IMDb page for more information.
  - Trailer URLs, reviews, or other relevant resources.

---

## Non-Functional Requirements

### 1. Performance:
- The app should load quickly by fetching movie/show data dynamically.
- Minimize reliance on large datasets stored locally; fetch up-to-date information from the API as needed.

### 2. Usability:
- The user interface should be simple, intuitive, and easy to navigate.
- The design should be responsive, adapting to both desktop and mobile screen sizes.

### 3. Reliability:
- Use reliable external APIs (like OMDb or TMDb) to ensure accurate and up-to-date data.
- Gracefully handle errors if data is not found or an API request fails.

---

## Development Milestones

### Phase 1 - Basic Search and Display:
- Implement search functionality with the Flask backend.
- Fetch movie/show data using the OMDb or TMDb API (IMDb ratings, basic details).
- Display basic information on the frontend (IMDb rating, cast, genre, etc.).
- Add a direct link to the IMDb Parents Guide.

### Phase 2 - Embedding Trailers and Light/Dark Mode:
- Implement embedded trailers for each movie/show (YouTube or IMDb).
- Add light/dark mode based on the user’s system theme and provide a toggle functionality.

### Phase 3 - Polish and External Links:
- Add more external links such as reviews, IMDb pages, and trailers.
- Test the application on various devices and browsers to ensure responsiveness.

---

## Achievements

- **Search Functionality**: Implemented a search bar that fetches dynamic movie/show information from the API.
- **IMDb Information**: Displayed IMDb ratings, cast, genre, year, runtime, and a link to the IMDb Parents Guide.
- **Embedded Trailers**: Successfully embedded trailers using YouTube and IMDb URLs.
- **Light/Dark Mode**: Theme auto-detection based on system preference and manual toggle button implemented.

---

## Future Enhancements

- Complete the dynamic light/dark mode feature with theme switching and storage of user preferences.

---

## Installation

### 1. Clone the Repository:
```bash
git clone <repository-url>
```


### 2. Set Up Virtual Environment:

It's recommended to use a virtual environment to manage dependencies.

- **Create a virtual environment** (if not already created):
    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      ```
    - On Windows:
      ```bash
      python -m venv venv
      ```

- **Activate the virtual environment**:
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```


### 3. Install Dependencies:

With the virtual environment activated, install the required dependencies:

```bash
pip install -r requirements.txt
```


### 4. Create .env File for API Keys:

To securely store your TMDb API key, create a `.env` file in the project root directory and add the following content:

```bash
TMDB_API_KEY=<your-tmdb-api-key>
```


### 5. Obtain TMDb API Key:

To get a TMDB API key:

-   Go to the [TMDb website](https://www.themoviedb.org/).
-   Create an account or log in if you already have one.
-   Navigate to the API section.
-   Click on "Create" to generate an API key.
-   Copy the API key and paste it into the `.env` file as shown above.


### 6. Run the Flask Application:

Once everything is set up, run the Flask application:

```
flask --app app.py --debug run
```

This will start the application, and you can view it in your browser at http://localhost:5000.

:)