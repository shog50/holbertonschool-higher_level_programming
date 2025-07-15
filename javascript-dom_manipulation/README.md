# JavaScript DOM Manipulation

This directory contains a series of JavaScript scripts that demonstrate the use of DOM manipulation, event handling, and API interaction using the Fetch API. The scripts are tested on the Chrome browser (v57 or later) and each interacts with the HTML DOM without reloading the page.

## 🛠️ General Requirements

- Allowed editors: All editors
- Files will be interpreted using **Chrome browser** (version 57.0+)
- All files end with a new line
- A mandatory `README.md` file is included with meaningful information
- Code follows **semistandard** style
- **No usage of `var`** is allowed (use `let` or `const`)
- DOM must be manipulated without reloading the page
- All interaction (text update, color change, fetching data) must be done via JavaScript and the DOM

## 📂 Files and Tasks

### `0-script.js`
- Updates the text color of the `<header>` element to red (`#FF0000`) using `document.querySelector`.

### `1-script.js`
- Changes the header text color to red when clicking the element with id `red_header`.

### `2-script.js`
- Adds the `red` class to the `<header>` element when the element with id `red_header` is clicked.

### `3-script.js`
- Toggles the `<header>` class between `red` and `green` when the element with id `toggle_header` is clicked.

### `4-script.js`
- Adds a new `<li>Item</li>` element to a list with the class `my_list` when the element with id `add_item` is clicked.

### `5-script.js`
- Changes the text content of the `<header>` to `"New Header!!!"` when the element with id `update_header` is clicked.

### `6-script.js`
- Fetches and displays the name of a Star Wars character (id: 5) from the URL `https://swapi-api.hbtn.io/api/people/5/?format=json` into the element with id `character`.

### `7-script.js`
- Fetches and displays a list of Star Wars movie titles from `https://swapi-api.hbtn.io/api/films/?format=json` into a `<ul>` with id `list_movies`.

### `8-script.js`
- Fetches the French translation of "Hello" from `https://hellosalut.stefanbohacek.dev/?lang=fr` and displays it in the element with id `hello`.
- This script is compatible with placement inside the `<head>` tag and waits for the DOM to load before executing.

## ✅ Usage

To test each script, use the corresponding HTML file (`0-main.html`, `1-main.html`, ..., `8-main.html`) and open it in a compatible browser.  
Each script is automatically loaded via the `<script src="X-script.js">` tag in the HTML.

## 🔍 Example

```html
<script type="text/javascript" src="3-script.js"></script>
#Author: Shouq Alosaimi

