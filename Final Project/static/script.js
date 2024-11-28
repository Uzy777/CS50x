// DOM Elements
const searchInput = document.getElementById("search-query");
const suggestionsDiv = document.getElementById("suggestions");
const movieDetailsDiv = document.getElementById("movie-details");

// Event Listeners
document.addEventListener("DOMContentLoaded", onPageLoad);
searchInput.addEventListener("input", onSearchInput);

// Load saved search query and trigger search on page load
function onPageLoad() {
    const savedSearchQuery = localStorage.getItem("searchQuery");
    if (savedSearchQuery) {
        searchInput.value = savedSearchQuery;
        searchMovies(savedSearchQuery); // Optionally, trigger search on page load
    }
}

// Handle user input in search bar and update suggestions
async function onSearchInput() {
    const query = searchInput.value.trim();
    if (query.length > 2) {
        localStorage.setItem("searchQuery", query); // Save the query to localStorage
        const data = await fetchSearchResults(query);
        updateSuggestions(data);
    } else {
        suggestionsDiv.innerHTML = ""; // Clear suggestions if query is too short
    }
}

// Fetch search results from API
async function fetchSearchResults(query) {
    const response = await fetch(`/search?query=${query}`);
    return await response.json();
}

// Update suggestions list
function updateSuggestions(data) {
    suggestionsDiv.innerHTML = "";
    if (data.length > 0) {
        data.forEach(item => {
            const suggestionItem = createSuggestionItem(item);
            suggestionsDiv.appendChild(suggestionItem);
        });
    }
}

// Create an individual suggestion item
function createSuggestionItem(item) {
    const div = document.createElement("div");
    div.classList.add("suggestion-item");
    div.innerHTML = `
        <img src="https://image.tmdb.org/t/p/w200${item.poster_path}" alt="${item.title}" width="50">
        ${item.title} (${item.release_date ? item.release_date.split("-")[0] : "N/A"})
    `;
    div.addEventListener("click", () => onSuggestionClick(item));
    return div;
}

// Handle click on a suggestion item
function onSuggestionClick(item) {
    showMovieDetails(item.id);
    suggestionsDiv.innerHTML = ""; // Clear suggestions on selection
}

// Display movie details
async function showMovieDetails(tmdbID) {
    const data = await fetchMovieDetails(tmdbID);
    movieDetailsDiv.innerHTML = generateMovieDetailsHTML(data);
    initializeCarousel();
    attachRecommendationListeners();
}

// Fetch movie details from API
async function fetchMovieDetails(tmdbID) {
    const response = await fetch(`/movie/${tmdbID}`);
    return await response.json();
}

// Generate movie details HTML
function generateMovieDetailsHTML(data) {
    return `
        <h2>${data.title} (${data.release_date ? data.release_date.split("-")[0] : "N/A"})</h2>
        <img src="https://image.tmdb.org/t/p/w500${data.poster_path}" alt="${data.title}" width="200">
        <p><strong>Rating:</strong> ${data.vote_average}/10</p>
        <p><strong>Plot:</strong> ${data.overview}</p>
        <p><strong>Genres:</strong> ${data.genres.map(genre => genre.name).join(", ")}</p>
        ${generateCastSection(data.cast)}
        ${generatePhotosSection(data.images)}
        ${generateTrailersSection(data.trailers)}
        ${generateRecommendationsSection(data.recommendations)}
    `;
}

// Generate Rotten Tomatoes section
// function generateRottenTomatoesSection(rottenTomatoes) {
//     if (rottenTomatoes) {
//         return `
//             <p><strong>Rotten Tomatoes:</strong></p>
//             <p><strong>Critic Score:</strong> ${rottenTomatoes.critic_score}</p>
//             <p><strong>Audience Score:</strong> ${rottenTomatoes.audience_score}</p>
//         `;
//     }
//     return "<p>No Rotten Tomatoes ratings available.</p>";
// }

// Generate Cast section
function generateCastSection(cast) {
    return `
        <h3>Cast:</h3>
        <div class="cast-container">
            ${cast.length > 0 ? cast.slice(0, 5).map(actor => createCastMemberHTML(actor)).join('') : 'No cast information available.'}
        </div>
    `;
}

// Create individual cast member HTML
function createCastMemberHTML(actor) {
    return `
        <div class="cast-member">
            <img src="https://image.tmdb.org/t/p/w200${actor.profile_path}" alt="${actor.name}" width="100">
            <div class="cast-info">
                <p class="actor-name"><strong>${actor.name}</strong></p>
                <p class="character-role">${actor.character ? `as ${actor.character}` : ''}</p>
            </div>
        </div>
    `;
}

// Generate Photos section (with Carousel)
function generatePhotosSection(images) {
    return `
        <h3>Photos:</h3>
        <div class="carousel-container">
            <button class="carousel-button prev" onclick="moveSlide(-1)">&#10094;</button>
            <div class="carousel-images">
                ${images.length > 0 ? images.map((image, index) => createCarouselSlideHTML(image, index)).join('') : 'No photos available.'}
            </div>
            <button class="carousel-button next" onclick="moveSlide(1)">&#10095;</button>
        </div>
    `;
}

// Create individual carousel slide HTML
function createCarouselSlideHTML(image, index) {
    return `
        <div class="carousel-slide" id="carousel-slide-${index}">
            <img src="https://image.tmdb.org/t/p/w500${image.file_path}" alt="Movie Photo" class="carousel-img">
        </div>
    `;
}

// Generate Trailers section
function generateTrailersSection(trailers) {
    return `
        <h3>Trailers:</h3>
        ${trailers.length > 0 ? trailers.slice(0, 3).map(trailer => createTrailerHTML(trailer)).join('') : "No trailers available."}
    `;
}

// Create individual trailer HTML
function createTrailerHTML(trailer) {
    return `
        <div class="trailer">
            ${trailer.key ? `
                <iframe width="600" height="350" src="https://www.youtube.com/embed/${trailer.key}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            ` : "<p>Trailer unavailable</p>"}
        </div>
    `;
}

// Generate Recommendations section
function generateRecommendationsSection(recommendations) {
    return `
        <h3>Recommendations:</h3>
        <div class="recommendation-list">
            ${recommendations.length > 0 ? recommendations.slice(0, 6).map(movie => createRecommendationHTML(movie)).join('') : 'No recommendations available.'}
        </div>
    `;
}

// Create individual recommendation HTML
function createRecommendationHTML(movie) {
    return `
        <div class="recommendation" data-movie-id="${movie.id}">
            <img src="https://image.tmdb.org/t/p/w200${movie.poster_path}" alt="${movie.title}" width="100">
            <p>${movie.title}</p>
        </div>
    `;
}

// Initialize Carousel
let slideIndex = 0;

function initializeCarousel() {
    const slides = document.querySelectorAll(".carousel-slide");
    if (slides.length > 0) {
        slideIndex = 0;
        updateCarousel();
    }
}

function moveSlide(step) {
    const slides = document.querySelectorAll(".carousel-slide");
    slideIndex += step;
    if (slideIndex < 0) slideIndex = slides.length - 1;
    else if (slideIndex >= slides.length) slideIndex = 0;
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
    recommendationItems.forEach(item => {
        item.addEventListener("click", async () => {
            const movieId = item.getAttribute("data-movie-id");
            showMovieDetails(movieId); // Display movie details for the clicked recommendation
        });
    });
}