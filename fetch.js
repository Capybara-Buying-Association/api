fetch("https://raw.githubusercontent.com/dolph/dictionary/master/popular.txt")
    .then(u => u.text())
    .then(data => {
        console.log({data: data.split("\n")})
    })