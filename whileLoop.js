function favoriteBooks (input){
    let favBook = input[0];

    let counter = 1;
    let bookIsFound = false;

    let nextBook = input[counter];
    while (nextBook !== "No More Books"){
        if (nextBook === favBook){
            bookIsFound = true;
            break;
        }
        counter++;
        nextBook = input[counter];
    }

    if (bookIsFound === false) {
        console.log("The book you search is not here!");
        console.log(`You checked ${counter - 1} books.`);
    } else {
        console.log(`You checked ${counter - 1} books and found it.`)
    }
}

favoriteBooks ([
"The Spot",
"Hunger Games",
"Harry Potter",
"Torronto",
"Spotify",
"No More Books"
])