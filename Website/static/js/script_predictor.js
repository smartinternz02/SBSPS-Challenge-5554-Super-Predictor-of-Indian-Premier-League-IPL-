document.addEventListener('DOMContentLoaded', function () {

    let data={}
    var select1 = document.querySelector(".team1")
    var select2 = document.querySelector(".team2")
    var tosswinner = document.querySelector("#validationServer06")

    function gen_tosslist() {
        var opt = document.createElement('option');
        opt.value = select1.options[select1.selectedIndex].value;
        opt.innerHTML = select1.options[select1.selectedIndex].innerHTML;
        tosswinner.appendChild(opt);
        var opt = document.createElement('option');
        opt.value = select2.options[select2.selectedIndex].value;
        opt.innerHTML = select2.options[select2.selectedIndex].innerHTML;
        tosswinner.appendChild(opt);

    }


    select1.addEventListener('change', function () {
        select1.classList.add('is-valid')
        select1.classList.remove('is-invalid')
        data['team1']=select1.options[select1.selectedIndex].value;
        select2.options[select1.selectedIndex].disabled = true;
        select2.style.display = "block";
        var msg = document.getElementById('validationServer03Feedback')
        msg.innerHTML = "Please select a valid team"
        select1.disabled = true;
    })
    select2.addEventListener('change', function () {
        select2.classList.add('is-valid')
        select2.classList.remove('is-invalid')
        select2.disabled = true;
        tosswinner.disabled = false;
        data['team2']=select2.options[select2.selectedIndex].value;
        document.getElementById('validationServer06Feedback').innerHTML = "Please select a valid team"
        gen_tosslist();

    })

    var toss = document.querySelector('#flexRadioDefault3')
    toss.addEventListener('change', function () {
        if (toss.checked == true) {
            document.getElementById('tosswinner').style.display = "block";
            document.getElementById('tossdecision').style.display = "block";
        }
    })

    var notoss = document.querySelector('#flexRadioDefault4')
    notoss.addEventListener('change', function () {
        if (notoss.checked == true) {
            document.getElementById('tosswinner').style.display = "none";
            document.getElementById('tossdecision').style.display = "none";

        }
    })

    let umpire1 = document.querySelector('#validationServer08')
    let umpire2 = document.querySelector('#validationServer09')
    let umpire3 = document.querySelector('#validationServer10')

    umpire1.addEventListener('change', function () {
        umpire1.disabled = true;
        let ump2opt = umpire2.options
        let ump3opt = umpire3.options;
        for (let i = 0; i < ump2opt.length; i++) {
            if (ump2opt[i].value == umpire1.options[umpire1.selectedIndex].value)
                ump2opt[i].disabled = true;
        }
        for (let i = 0; i < ump3opt.length; i++) {
            if (ump3opt[i].value == umpire1.options[umpire1.selectedIndex].value)
                ump3opt[i].disabled = true;
        }
        data['umpire1']=umpire1.options[umpire1.selectedIndex].value;
        umpire3.options[umpire1.selectedIndex].value.disabled = true;
        umpire2.disabled = false;
    })

    umpire2.addEventListener('change', function () {
        umpire2.disabled = true;
        let ump3opt = umpire3.options;
        for (let i = 0; i < ump3opt.length; i++) {
            if (ump3opt[i].value == umpire2.options[umpire2.selectedIndex].value)
                ump3opt[i].disabled = true;
        }
        data['umpire2']=umpire2.options[umpire2.selectedIndex].value;
        umpire3.options[umpire1.selectedIndex].value.disabled = true;
        umpire3.disabled = false;
    })

    var select = document.querySelectorAll('.other');
    for (let i = 0; i < select.length; i++) {
        select[i].addEventListener('change', function () {
            let eleid = select[i].id + "Feedback"
            let ele = document.getElementById(eleid)
            ele.classList.add('valid-feeedback')
            ele.classList.remove('invalid-feeedback')
            select[i].classList.add('is-valid')
            select[i].classList.remove('is-invalid')
            select[i].disabled = true;

        })
    }
    let btn = document.getElementById('btn')
    if (btn) {
        btn.addEventListener('click', function () {
            data['venue']=document.querySelector("#validationServer04").options[document.querySelector("#validationServer04").selectedIndex].value
            data['umpire3']=umpire3.options[umpire3.selectedIndex].value;
            if(toss.checked==true)
            {
                data['tossch']=true;
                data['tosswinner']=document.querySelector("#validationServer06").options[document.querySelector("#validationServer06").selectedIndex].value
                if(document.querySelector("#flexRadioDefault1").checked==true)
                    data['tossdec']='bat';
                else
                    data['tossdec']='field';   
            }
            else
            {
                data['tossch']=false
                data['tosswinner']=null;
                data['tossdec']=null;
            }
            post('/submit', data);
        })
    }
})

function post(path, params, method = 'post') {

    // The rest of this code assumes you are not using a library.
    // It can be made less verbose if you use one.
    const form = document.createElement('form');
    form.method = method;
    form.action = path;

    for (const key in params) {
        if (params.hasOwnProperty(key)) {
            const hiddenField = document.createElement('input');
            hiddenField.type = 'hidden';
            hiddenField.name = key;
            hiddenField.value = params[key];

            form.appendChild(hiddenField);
        }
    }
    document.getElementById('form').style.display='none';
    document.getElementById('loader').style.display='flex';
    document.body.appendChild(form);
    form.submit();
}
