//
//  AsignaturasTableViewCell.swift
//  Profesorado
//
//  Created by Flavius Stan on 3/1/18.
//  Copyright © 2018 Flavius Stan. All rights reserved.
//

import UIKit

class AsignaturasTableViewCell: UITableViewCell {

    
    @IBOutlet weak var NomAsignatura: UILabel!
    @IBOutlet weak var ActaAsignatura: UIButton!
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }
    @IBAction func EntrarEnActa(_ sender: Any) {
        NomAsignatura.text="Hola"
    }
    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
