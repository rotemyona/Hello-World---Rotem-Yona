fetch('https://reqres.in/api/users?page=2').then(response=>response.json()).then(responseJSON => creatUserList(responseJSON.data)).catch(err => console.log(err));


function creatUserList(users){
    console.log(users);
    const curr_main = document.querySelector("main");
    for (let user of users){
        const section = document.createElement("section");
        section.innerHTML = `
        <img src = "${user.avatar}" alt  ="profile picture"/>    
        <div>
            <span>${user.first_name} ${user.last_name}</span>
            <br>
            <a href="mailto:${user.email}">Sent Email</a>
        </div>
        `;
        curr_main.appendChild(section);
    }
}