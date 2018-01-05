//
//  AsignaturaTableViewController.swift
//  Profesorado
//
//  Created by Flavius Stan on 3/1/18.
//  Copyright © 2018 Flavius Stan. All rights reserved.
//

import UIKit

class AsignaturaTableViewController: UITableViewController {
    //Variables
    
    var asignaturas = [Asignatura]()
    override func viewDidLoad() {
        super.viewDidLoad()
        loadSampleAsignaturas()
        self.tableView.register(UITableViewCell.self, forCellReuseIdentifier: "AsignaturasTableViewCell")
        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem
    }
    private func loadSampleAsignaturas(){
        let asignatura1 = "Matematicas"
        let asignatura2 = "Programacion"
        
        let asignaturaO1 = Asignatura( asignatura: asignatura1,id : 1)
        let asignaturaO2 = Asignatura( asignatura: asignatura2, id : 2)
        
        asignaturas += [asignaturaO1,asignaturaO2]
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return asignaturas.count
    }

    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cellIdentifier = "AsignaturasTableViewCell"
        
        guard let cell = tableView.dequeueReusableCell(withIdentifier: cellIdentifier, for: indexPath) as? AsignaturasTableViewCell else{
            fatalError("The dequeued cell is not an instance of MealTableViewCell.")
        }
        let asignatura = asignaturas[indexPath.row]
        cell.NomAsignatura.text = asignatura.nombre

        return cell
    }
 

    /*
    // Override to support conditional editing of the table view.
    override func tableView(_ tableView: UITableView, canEditRowAt indexPath: IndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCellEditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {
            // Delete the row from the data source
            tableView.deleteRows(at: [indexPath], with: .fade)
        } else if editingStyle == .insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(_ tableView: UITableView, moveRowAt fromIndexPath: IndexPath, to: IndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(_ tableView: UITableView, canMoveRowAt indexPath: IndexPath) -> Bool {
        // Return false if you do not want the item to be re-orderable.
        return true
    }
    */

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}