// bookmark.js

// Load bookmarks from localStorage or create an empty array
function loadBookmarks() {
    const bookmarks = localStorage.getItem('bookmarkedRecipes');
    return bookmarks ? JSON.parse(bookmarks) : [];
}

// Save bookmarks back to localStorage
function saveBookmarks(bookmarks) {
    localStorage.setItem('bookmarkedRecipes', JSON.stringify(bookmarks));
}

// Check if a recipe is bookmarked
function isBookmarked(recipeId) {
    const bookmarks = loadBookmarks();
    return bookmarks.some(recipe => recipe.id === recipeId);
}

// Toggle bookmark for a recipe
function toggleBookmark(recipe) {
    let bookmarks = loadBookmarks();
    const index = bookmarks.findIndex(item => item.id === recipe.id);

    if (index > -1) {
        // Remove bookmark
        bookmarks.splice(index, 1);
    } else {
        // Add bookmark
        bookmarks.push(recipe);
    }
    saveBookmarks(bookmarks);
    updateBookmarkButton(recipe.id);
}

// Update bookmark button UI
function updateBookmarkButton(recipeId) {
    const btns = document.querySelectorAll(`.bookmark-btn[data-recipe-id="${recipeId}"]`);
    btns.forEach(btn => {
        if (isBookmarked(recipeId)) {
            btn.textContent = '❤️ Bookmarked';
            btn.classList.add('bookmarked');
        } else {
            btn.textContent = '🤍 Bookmark';
            btn.classList.remove('bookmarked');
        }
    });
}

// Initialize bookmark buttons on page load
function initBookmarks() {
    const buttons = document.querySelectorAll('.bookmark-btn');

    buttons.forEach(btn => {
        const recipeId = parseInt(btn.getAttribute('data-recipe-id'));
        const title = btn.getAttribute('data-title');
        const image = btn.getAttribute('data-image');

        // Set initial button state
        updateBookmarkButton(recipeId);

        // Attach click handler
        btn.addEventListener('click', () => {
            toggleBookmark({ id: recipeId, title, image });
        });
    });
}

// Run on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    initBookmarks();
});
