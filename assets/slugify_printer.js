const ser_numInput = document.querySelector('input[name=ser_num]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')   // replace & with -and-
        .replace(/[\s\W-]+/g, '-')   // replace spaces
};


ser_numInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(ser_numInput.value));
});