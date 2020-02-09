window.onload=function()	{

		patient=[
				{
					"name":"Rahul",
					"aadhar":"1239603923",
					"tests":['ABC','XYZ','DPT'],
					"hosp":"JUHU Hospital"
				},
	
				{
					"name":"Koyna",
					"aadhar":"12459203923",
					"tests":['DEF','LOR','LOP'],
					"hosp":"CMH Hospital"
				},
	
				{
					"name":"Dhriti",
					"aadhar":"1239203823",
					"tests":['JUX','KOL','LOH'],
					"hosp":"Fortis Hospital"
				}
			]

			hospital=[
				{
					"name":"JUHU Hospital",
					"loc":"Mumbai"
				},
				{
					"name":"CMH Hospital",
					"loc":"Bangalore"
				},
				{
					"name":"Fortis Hospital",
					"loc":"Delhi"
				}
			]
	
	
		hospital.forEach(function(item,index)	{
			elem=document.createElement("th");
			elem.id=item.name;
			elem.innerHTML=item.name;
			document.getElementById("menu").appendChild(elem);
		})
	
		
		hospital.forEach(mouseEventHandler);
	
		function mouseEventHandler(item,index){
			elem=document.getElementById(item.name);
			document.getElementById("data-elements").removeAttribute("hidden");
					patient.forEach(function(item,index){
						if(elem.id==item.hosp){
							elem.onmouseover=function ()
							{
							if(item.hosp=="CMH Hospital")
							document.getElementById('chngclr').style.color = 'cyan'
							else if (item.hosp=="JUHU Hospital")
							document.getElementById('chngclr').style.color = 'magenta'
							else 
							document.getElementById('chngclr').style.color = 'orange'
							
							details=item;
							document.getElementById("name").innerHTML=details.name;
							document.getElementById("aadhar").innerHTML=details.aadhar;
							document.getElementById("tests").innerHTML=details.tests[0]+","+details.tests[1]+","+details.tests[2];
						}
					}
				})
		}
	};