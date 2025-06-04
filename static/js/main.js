document.addEventListener('DOMContentLoaded', () => {
    const bookmarkButtons = document.querySelectorAll('.bookmark-btn');

    bookmarkButtons.forEach(button => {
        button.addEventListener('click', () => {
            const recipeId = button.dataset.recipeId;
            const title = button.dataset.title;
            const image = button.dataset.image;

            const favorites = JSON.parse(localStorage.getItem('favorites')) || [];
            const exists = favorites.some(fav => fav.id === recipeId);

            if (!exists) {
                favorites.push({ id: recipeId, title, image });
                localStorage.setItem('favorites', JSON.stringify(favorites));
                alert('Recipe added to favorites!');
            } else {
                alert('Already in favorites');
            }
        });
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('recipeModal');
    const modalBody = document.getElementById('modal-body');
    const closeBtn = document.querySelector('.close-btn');

    document.querySelectorAll('.modal-link').forEach(link => {
        link.addEventListener('click', async (e) => {
            e.preventDefault();
            const recipeId = link.dataset.recipeId;

            modal.style.display = "block";
            modalBody.innerHTML = "<div class='loader'></div>";

            try {
                const res = await fetch(`/api/recipe/${recipeId}`);
                const data = await res.json();
                modalBody.innerHTML = `
            <h2>${data.title}</h2>
            <img src="${data.image}" style="max-width:100%">
            <p>${data.summary || 'No summary available.'}</p>
          `;
            } catch (err) {
                modalBody.innerHTML = "<p>Error loading recipe.</p>";
            }
        });
    });

    closeBtn.onclick = () => modal.style.display = "none";
    window.onclick = (e) => { if (e.target == modal) modal.style.display = "none"; };
});
    