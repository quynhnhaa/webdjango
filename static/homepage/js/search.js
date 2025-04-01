document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.querySelector('.search-wrapper input[type="search"]');
    const closeBtn = document.querySelector('.search-wrapper .close-btn');
    const items = document.querySelectorAll(".single-blog-area");

    // Lọc món ăn khi nhập vào ô tìm kiếm
    searchInput.addEventListener("input", function() {
        const query = this.value.toLowerCase();
        items.forEach(item => {
            const title = item.querySelector(".post-title").innerText.toLowerCase();
            item.style.display = title.includes(query) ? "" : "none";
        });
    });

    // Xóa nội dung tìm kiếm khi nhấn nút đóng
    closeBtn.addEventListener("click", function() {
        searchInput.value = "";
        items.forEach(item => item.style.display = ""); 
    });
});

// document.addEventListener("DOMContentLoaded", function() {
//     const searchForm = document.getElementById("searchForm");
//     const searchInput = document.getElementById("searchInput");

//     searchForm.addEventListener("submit", function(event) {
//         event.preventDefault(); // Ngăn form gửi request GET

//         const query = searchInput.value.trim();
//         const url = new URL(window.location);
//         const params = new URLSearchParams(url.search);

//         if (query) {
//             params.set('search', query);
//         } else {
//             params.append('search');
//         }

//         window.history.replaceState({}, '', '?' + params.toString());
//     });
// });