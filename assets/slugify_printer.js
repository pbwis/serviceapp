const idInput = document.querySelector('input[name=ser_num]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')
        .replace(/[\s\W-]+/g, '-')
};

ser_numInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(ser_numInput.value));
});