//
//  ViewController.swift
//  Profesorado
//
//  Created by Flavius Stan on 26/12/17.
//  Copyright © 2017 Flavius Stan. All rights reserved.
//

import UIKit
import LocalAuthentication
class ViewController: UIViewController {

    @IBOutlet weak var Nombre: UITextField!
    @IBOutlet weak var Contraseña: UITextField!
    @IBOutlet weak var Login: UIButton!
    @IBOutlet weak var Bio: UIButton!
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view, typically from a nib.
    }
    @IBAction func ánalisis(_ sender: Any) {
        loginFinger()
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    private func loginFinger(){
        let context:LAContext = LAContext()
        
        if context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: nil){
            context.evaluatePolicy(LAPolicy.deviceOwnerAuthenticationWithBiometrics, localizedReason: "Por favor inicie sesion", reply: { (succesful, error) in
                if succesful{
                    let storyboard = UIStoryboard(name: "Main", bundle: nil)
                    let vc = storyboard.instantiateViewController(withIdentifier: "LoginCorrecto")
                    self.present(vc, animated: true, completion: nil)
                }
                else{
                    print("Error")
                }
            })
        }
        
        
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

