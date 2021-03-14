const idInput = document.querySelector('input[name=id]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')   // replace & with -and-
        .replace(/[\s\W-]+/g, '-')   // replace spaces
};


idInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(idInput.value));
});