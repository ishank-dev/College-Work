window.onload = () =>{
    var jsonobj = [
        {
            "name":"Rohit",
            "country":"Gitland",
            "title":"Hackerman",
            "year":"3000"
        },
        {
            "name":"Reshma",
            "country":"USA-LA",
            "title":"Haunted",
            "year":"2050"
        },
        {
            "name":"Nikhil Zombie",
            "country":"The dark",
            "title":"Deadland",
            "year":"2021"
        },
        {
            "name":"Shreekumar",
            "country":"South Africa",
            "title":"Surviving in Africa",
            "year":"2019"
        }
    ]
    
    jsonobj.forEach(function dothis(item,index){
        if(index<=1){
            var def = document.createElement('tr')
            var a =  document.createElement('td')
            a.innerHTML = item.name
            var b =  document.createElement('td')
            b.innerHTML = item.country
            var c =  document.createElement('td')
            c.innerHTML = item.year
            var d =  document.createElement('td')
            d.innerHTML = item.title
           
            def.appendChild(a)
            def.appendChild(b)
            def.appendChild(c)
            def.appendChild(d)
            document.getElementById('auth').appendChild(def)
    }
        else{
            var abc = document.createElement('p')
            abc.innerHTML = item.name+"\t|\t"+item.country+"\t|\t"+item.year+"\t|\t"+item.title+"|" 
            document.getElementById('auth1').appendChild(abc)
        }
    })
}