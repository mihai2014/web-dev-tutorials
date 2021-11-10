function showTabSelection() {

    let fileName = ""

    //scan all tab buttons with id = "button-*" and get current selection
    var buttons = document.getElementsByTagName('button');
    for (let i = 0; i < buttons.length; i++) {
        let button = buttons[i];
        if(button.id.split("-")[0] == "button") {
            if(button.getAttribute('active') == "true") {
                // console.log('current: '+button.id.split("-")[1]);
                fileName = button.id.split("-")[1];
            }
        }
    }    

    //scan all paragraphs with id = "file-*"
    var divs = document.getElementsByTagName('div'); 
    for (let i = 0; i < divs.length; i++) {
        let div = divs[i];
        if(div.id.split("-")[0] == "file") {
            // console.log(div.id.split("-")[1]);
            fileTopic = div.id.split("-")[1];
            if(fileTopic == fileName) {
                div.setAttribute("class", "visible");
            } else {
                div.setAttribute("class", "invisible");
            }
        }
    } 

}

showTabSelection()

function changeSelection() {

    const selected    = 'text-gray-600 py-4 px-10 block hover:text-blue-500 focus:outline-none\
    text-blue-500 border-b-2 font-medium border-blue-500'
    const notSelected = 'text-gray-600 py-4 px-10 block hover:text-blue-500 focus:outline-none'    

    // console.log("current"+" "+this.id);

    var buttons = document.getElementsByTagName('button');
    for (let i = 0; i < buttons.length; i++) {
        let button = buttons[i];
        // console.log(button.id);  
        if(button.id == this.id) {
            button.setAttribute("active","true");   
            button.setAttribute("class",selected);   
        } else {
            button.setAttribute("active","false");   
            button.setAttribute("class",notSelected);   
        }
    }

    showTabSelection();
}

function initSelectTab() {
    var buttons = document.getElementsByTagName('button');
    for (let i = 0; i < buttons.length; i++) {
        let button = buttons[i];    
        button.onclick = changeSelection;
    }    
}

initSelectTab();

