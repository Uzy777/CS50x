const searchInput = document.getElementById("search-query");
const suggestionsDiv = document.getElementById("suggestions");
const movieDetailsDiv = document.getElementById("movie-details");

// Retrieve the search query from localStorage and set it in the input field on page load
document.addEventListener("DOMContentLoaded", () => {
    const savedSearchQuery = localStorage.getItem("searchQuery");
    if (savedSearchQuery) {
        searchInput.value = savedSearchQuery;
        searchMovies(savedSearchQuery); // Optionally, trigger search on page load
    }
});

// Listen for user input in the search bar
searchInput.addEventListener("input", async () => {
    const query = searchInput.value.trim();
    if (query.length > 2) {
        // Save the query to localStorage
        localStorage.setItem("searchQuery", query);

        // Make API call to search movies
        const response = await fetch(`/search?query=${query}`);
        const data = await response.json();
        suggestionsDiv.innerHTML = "";

        if (data.length > 0) {
            data.forEach((item) => {
                const div = document.createElement("div");
                div.classList.add("suggestion-item");
                div.innerHTML = `
                    <img src="https://image.tmdb.org/t/p/w200${item.poster_path}" alt="${item.title}" width="50">
                    ${item.title} (${item.release_date ? item.release_date.split("-")[0] : "N/A"})
                `;
                div.addEventListener("click", () => {
                    showMovieDetails(item.id);
                    suggestionsDiv.innerHTML = ""; // Clear suggestions on selection
                });
                suggestionsDiv.appendChild(div);
            });
        }
    } else {
        suggestionsDiv.innerHTML = ""; // Clear suggestions if query is too short
    }
});

// Fetch and display movie details
async function showMovieDetails(tmdbID) {
    const response = await fetch(`/movie/${tmdbID}`);
    const data = await response.json();

    // Populate the movie details
    movieDetailsDiv.innerHTML = `
        <h2>${data.title} (${data.release_date ? data.release_date.split("-")[0] : "N/A"})</h2>
        <img src="https://image.tmdb.org/t/p/w500${data.poster_path}" alt="${data.title}" width="200">
        ${data.parents_guide_url ? `<p><strong><a href="${data.parents_guide_url}" target="_blank">Parents Guide</a></strong></p>` : ""}
        <p><strong>Rating:</strong> ${data.vote_average}/10</p>
        <p><strong>Plot:</strong> ${data.overview}</p>
        <p><strong>Genres:</strong> ${data.genres.map((genre) => genre.name).join(", ")}</p>

        <!-- Cast Section -->
        <h3>Cast:</h3>
        <div class="cast-container">
            ${data.cast.length > 0 ? data.cast.slice(0, 5).map(actor => `
                <div class="cast-member">
                    <img src="https://image.tmdb.org/t/p/w200${actor.profile_path}" alt="${actor.name}" width="100">
                    <div class="cast-info">
                        <p class="actor-name"><strong>${actor.name}</strong></p>
                        <p class="character-role">${actor.character ? `as ${actor.character}` : ''}</p>
                    </div>
                </div>
            `).join('') : 'No cast information available.'}
        </div>

        <!-- Photos Section (with Carousel) -->
        <h3>Photos:</h3>
        <div class="carousel-container">
            <button class="carousel-button prev" onclick="moveSlide(-1)">&#10094;</button>
            <div class="carousel-images">
                ${
                    data.images.length > 0
                        ? data.images
                              .map(
                                  (image, index) => `
                    <div class="carousel-slide" id="carousel-slide-${index}">
                        <img src="https://image.tmdb.org/t/p/w500${image.file_path}" alt="Movie Photo" class="carousel-img">
                    </div>
                `
                              )
                              .join("")
                        : "No photos available."
                }
            </div>
            <button class="carousel-button next" onclick="moveSlide(1)">&#10095;</button>
        </div>

        <!-- Trailers Section -->
        <h3>Trailers:</h3>
        ${
            data.trailers.length > 0
                ? data.trailers
                      .slice(0, 3)
                      .map(
                          (trailer) => `
            <div class="trailer">
                ${trailer.key ? `
                    <iframe width="600" height="350" src="https://www.youtube.com/embed/${trailer.key}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                ` : "<p>Trailer unavailable</p>"}
            </div>
        `
                      )
                      .join("")
                : "No trailers available."
        }

        <!-- Recommendations Section -->
        <h3>Recommendations:</h3>
        <div class="recommendation-list">
            ${
                data.recommendations.slice(0, 6).length > 0
                    ? data.recommendations
                          .slice(0, 6)
                          .map(
                              (movie) => `
                <div class="recommendation" data-movie-id="${movie.id}">
                    <img src="https://image.tmdb.org/t/p/w200${movie.poster_path}" alt="${movie.title}" width="100">
                    <p>${movie.title}</p>
                </div>
            `
                          )
                          .join("")
                    : "No recommendations available."
            }
        </div>
    `;

    // Initialize carousel to show the first image
    initializeCarousel();

    // Re-attach recommendation click listeners
    attachRecommendationListeners();
}

// Carousel functions
let slideIndex = 0;

function initializeCarousel() {
    const slides = document.querySelectorAll(".carousel-slide");

    if (slides.length > 0) {
        slideIndex = 0; // Start with the first slide
        updateCarousel();
    }
}

function moveSlide(step) {
    const slides = document.querySelectorAll(".carousel-slide");
    slideIndex += step;

    if (slideIndex < 0) {
        slideIndex = slides.length - 1;
    } else if (slideIndex >= slides.length) {
        slideIndex = 0;
    }

    updateCarousel();
}

function updateCarousel() {
    const slides = document.querySelectorAll(".carousel-slide");
    slides.forEach((slide, index) => {
        slide.style.display = index === slideIndex ? "block" : "none";
    });
}

// Attach click listeners to recommendations
function attachRecommendationListeners() {
    const recommendationItems = document.querySelectorAll(".recommendation");
    recommendationItems.forEach((item) => {
        item.addEventListener("click", async () => {
            const movieId = item.getAttribute("data-movie-id");
            showMovieDetails(movieId); // Display movie details for the clicked recommendation
        });
    });
}

// Attach recommendation listeners on initial load
document.addEventListener("DOMContentLoaded", () => {
    attachRecommendationListeners();
});