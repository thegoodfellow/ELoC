function showHideStuff () {
    if(document.getElementById('type').toString() == 'student'){
        document.getElementById('degreeGroup').style.display='none';
        document.getElementById('degree').style.display='none';
        document.getElementById('test').style.display='none';
    }
    else{
        document.getElementById('degreeGroup').style.display='block';
        document.getElementById('degree').style.display='block';
    }
}