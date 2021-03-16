<?php
// Class that provides methods for working with the form data.
// There should be NOTHING in this file except this class definition.

class SimpleController {
	private $mapper; // 变量外部不可见
	
	public function __construct() { // __PHP内置函数，对象被创建时，function run
		global $f3;						// needed for $f3->get()
		// $this表示this object
		$this->mapper = new DB\SQL\Mapper($f3->get('DB'),"episode");// create DB query mapper object
																			// for the "simpleModel" table
	}
	
	public function putIntoDatabase($data) {	// public 的函数
		$this->mapper->name = $data["name"];					// set value for "name" field
		$this->mapper->episode1 = $data["episode1"];
		$this->mapper->episode2 = $data["episode2"];				// set value for "colour" field
		$this->mapper->episode3 = $data["episode3"];				// set value for "colour" field
// set value for "colour" field
		$this->mapper->save();									// save new record with these fields
	}
	
	public function getData() {
		$list = $this->mapper->find();
		return $list;
	}
	
	public function deleteFromDatabase($idToDelete) {
		$this->mapper->load(['id=?', $idToDelete]);				// load DB record matching the given ID
		$this->mapper->erase();									// delete the DB record
	}
	
}

?>
