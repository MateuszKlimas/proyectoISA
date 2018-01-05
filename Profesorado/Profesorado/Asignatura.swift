//
//  Asignatura.swift
//  Profesorado
//
//  Created by Flavius Stan on 3/1/18.
//  Copyright © 2018 Flavius Stan. All rights reserved.
//

import UIKit

class Asignatura: NSObject {
    var nombre = ""
    var idAsignatura = 0
    
    init(asignatura : String,id : Int) {
        self.nombre = asignatura
        self.idAsignatura = id
    }
}
