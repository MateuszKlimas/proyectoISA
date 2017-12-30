//
//  ViewController.swift
//  Profesorado
//
//  Created by Flavius Stan on 26/12/17.
//  Copyright © 2017 Flavius Stan. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var Nombre: UITextField!
    @IBOutlet weak var Contraseña: UITextField!
    @IBOutlet weak var Login: UIButton!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func ErraseName(_ sender: Any) {
        Nombre.text = ""
    }
    @IBAction func ErrasePassw(_ sender: Any) {
        Contraseña.text = ""
    }
    @IBAction func EnteredPressed(_ sender: Any) {
        if Nombre.text=="Flavius" && Contraseña.text=="12340"{
            let storyboard = UIStoryboard(name: "Main", bundle: nil)
            let vc = storyboard.instantiateViewController(withIdentifier: "LoginCorrecto")
            self.present(vc, animated: true, completion: nil)
        }
    }
    
    @IBAction func hacerLogin(_ sender: Any) {
        if Nombre.text=="Flavius" && Contraseña.text=="12340"{
            let storyboard = UIStoryboard(name: "Main", bundle: nil)
            let vc = storyboard.instantiateViewController(withIdentifier: "LoginCorrecto")
            self.present(vc, animated: true, completion: nil)
        }
    }
    
}

