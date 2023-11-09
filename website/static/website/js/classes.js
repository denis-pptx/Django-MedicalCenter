function log_decorator(func) {
    function wrapper(...params) {
        console.log(`${new Date().toISOString()} | ${func.name}`);
        return func.apply(this, params);
    }
    
    return wrapper;
}

function Human(name, age) {
    let _name = name;
    let _age = age;

    this.name = function(name) {
        if (name == undefined)
            return _name;
        else
            _name = name;
    }

    this.age = function(age) {
        if (age == undefined)
            return _age;
        else 
            _age = age;
    }

    this.toString = function() {
        return `Human\n`+
                `name: ${this.name()}\n`+
                `age: ${this.age()}\n`;
    }
}

function Doctor(name, age, specialization) {
    this.__proto__ = new Human(name, age);

    let _specialization = specialization;

    this.specialization = function specealizationProperty(specialization) {
        if (specialization == undefined)
            return _specialization;
        else
            _specialization = specialization;
    }

    this.specialization = log_decorator(this.specialization);

    this.toString = function() {
        return `Doctor\n`+
                `name: ${this.name()}\n`+
                `age: ${this.age()}\n`+
                `specialization: ${this.specialization()}`;
    }
}

// class Human {
//     constructor(name, age) {
//         this._name = name;
//         this._age = age;
//     }

//     name(name) {
//         if (name == undefined)
//             return this._name;
//         else
//             this._name = name;
//     }

//     age(age) {
//         if (age == undefined)
//             return this._age;
//         else 
//             this._age = age;
//     }

//     toString() {
//         return `Human\n`+
//         `name: ${this.name()}\n`+
//         `age: ${this.age()}\n`;
//     }
// }


// class Doctor extends Human {
//     constructor(name, age, specialization) {
//         super(name, age);
//         this._specialization = specialization;
//     }

//     specialization(specialization) {
//         if (specialization == undefined)
//             return this._specialization;
//         else
//            this._specialization = specialization;
//     }

//     toString() {
//         return `Doctor\n`+
//                 `name: ${this.name()}\n`+
//                 `age: ${this.age()}\n`+
//                 `specialization: ${this.specialization()}`;
//     }
// }
// Doctor.prototype.specialization = log_decorator(Doctor.prototype.specialization);

const demo = document.getElementById('demo');

let human = new Human('Denis', 19);
human.age(20);
human.name('Denis Konchik')
demo.innerHTML += `
    <b>human:</b><br>
    human.name(): ${human.name()}<br>
    human.age(): ${human.age()} <br>
    human.toString(): ${human.toString()}
`;

let doctor = new Doctor('Ivan', 40, 'pediatr');
doctor.age(60);
doctor.specialization('terapevt');
demo.innerHTML += `
    <br><br>
    <b>doctor:</b><br>
    doctor.name(): ${doctor.name()}<br>
    doctor.age(): ${doctor.age()} <br>
    doctor.specialization(): ${doctor.specialization()} <br>
    doctor.toString(): ${doctor.toString()}
`;
