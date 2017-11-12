import os

def get_folder():
    folder_name = input("Enter the absolute path to the Java model folder: ")
    return folder_name

def get_project_name():
    project_name = input("Enter the project name: ")
    project_name = project_name.lower()
    return project_name

def iterate(folder, project_name):
    os.mkdir("repository")
    os.mkdir("service")
    os.mkdir("controller")
    for file_name in os.listdir(folder):
        if file_name.endswith(".java"):
            class_name = file_name[0:-5]
            
            service_file = open("service" + os.sep + class_name + "Service.java", "w")
            service_file.write(create_service(class_name, project_name))
            service_file.close()

            service_impl_file = open("service" + os.sep + class_name + "ServiceImpl.java", "w")
            service_impl_file.write(create_service_impl(class_name, project_name))
            service_impl_file.close()

            repository_file = open("repository" + os.sep + class_name + "Repository.java", "w")
            repository_file.write(create_repository(class_name, project_name))
            repository_file.close()

            controller_file = open("controller" + os.sep + class_name + "Controller.java", "w")
            controller_file.write(create_controller(class_name, project_name))
            controller_file.close()
        else:
            continue



def create_repository(class_name, project_name):
    content = """package com.""" + project_name + """.repository;\n\nimport org.springframework.data.jpa.repository.JpaRepository;\n\nimport com.""" + project_name + """.domain.""" + class_name + """;\n\npublic interface """ + class_name + """Repository extends JpaRepository<""" + class_name + """, Long> {\n\n}"""
    return content

def create_service(class_name, project_name):
    var_name = class_name.lower()
    content = """package com.""" + project_name + """.service;\n\nimport java.util.Collection;\n\nimport com.""" + project_name + """.domain.""" + class_name + """;\n\npublic interface """ + class_name + """Service {\n\n\tCollection<""" + class_name + """> findAll();\n\n\t""" + class_name + """ findOne(Long id);\n\n\t""" + class_name + """ create(""" + class_name + """ """ + var_name + """) throws Exception;\n\n\t""" + class_name + """ update(""" + class_name + """ """ + var_name + """) throws Exception;\n\n\tvoid delete(""" + class_name + """ """ + var_name + """) throws Exception;\n\n}"""
    return content
def create_service_impl(class_name, project_name):
    var_name = class_name.lower()
    content = """package com.""" + project_name + """.service;

import java.util.Collection;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.""" + project_name + """.domain.""" + class_name + """;
import com.""" + project_name + """.repository.""" + class_name + """Repository;

@Service
public class """ + class_name + """ServiceImpl implements """ + class_name + """Service{
	
	@Autowired
	private """ + class_name + """Repository """ + var_name + """Repository;

	@Override
	public Collection<""" + class_name + """> findAll() {
		// TODO Auto-generated method stub
		return """ + var_name + """Repository.findAll();
	}

	@Override
	public """ + class_name + """ findOne(Long id) {
		// TODO Auto-generated method stub
		return """ + var_name + """Repository.findOne(id);
	}

	@Override
	public """ + class_name + """ create(""" + class_name + """ """ + var_name + """) throws Exception {
		// TODO Auto-generated method stub
		return """ + var_name + """Repository.save(""" + var_name + """);
		
	}

	@Override
	public """ + class_name + """ update(""" + class_name + """ """ + var_name + """) throws Exception {
		// TODO Auto-generated method stub
		return """ + var_name + """Repository.save(""" + var_name + """);
	}

	@Override
	public void delete(""" + class_name + """ """ + var_name + """) throws Exception {
		// TODO Auto-generated method stub
		""" + var_name + """Repository.delete(""" + var_name + """);
		
	}

	
}
"""
    return content

def create_controller(class_name, project_name):
    var_name = class_name.lower()
    content = """package com.""" + project_name + """.controller;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import com.""" + project_name + """.domain.""" + class_name + """;
import com.""" + project_name + """.service.""" + class_name + """Service;

@RestController
@RequestMapping(value = "/""" + var_name + """")
public class """ + class_name + """Controller {

	@Autowired
	private final """ + class_name + """Service """ + var_name + """Service;
	
	public """ + class_name + """Controller(""" + class_name + """Service """ + var_name + """Service) {
		this.""" + var_name + """Service = """ + var_name + """Service;
	}
	
	@CrossOrigin
	@RequestMapping(value = "/create", 
	method = RequestMethod.POST,
	consumes = MediaType.APPLICATION_JSON_VALUE,
	produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<""" + class_name + """> create""" + class_name + """(@RequestBody """ + class_name + """ """ + var_name + """)
    {
		""" + class_name + """ exists = """ + var_name + """Service.findOne(""" + var_name + """.getId());
		
		if(exists != null){
			return new ResponseEntity<""" + class_name + """>(HttpStatus.CONFLICT);
		}
        
		""" + class_name + """ saved = null;
		try {
			saved = """ + var_name + """Service.create(""" + var_name + """);
		} catch (Exception e) {
			e.printStackTrace();
		}
        return new ResponseEntity<""" + class_name + """>(saved, HttpStatus.CREATED);
    }
	
	@CrossOrigin
	@RequestMapping(value = "/update", 
	method = RequestMethod.PUT,
	consumes = MediaType.APPLICATION_JSON_VALUE,
	produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<""" + class_name + """> update""" + class_name + """(@RequestBody """ + class_name + """ """ + var_name + """)
    {
		""" + class_name + """ exists = """ + var_name + """Service.findOne(""" + var_name + """.getId());
		
		if(exists == null){
			return new ResponseEntity<""" + class_name + """>(HttpStatus.NOT_FOUND);
		}
        
		""" + class_name + """ saved = null;
		try {
			saved = """ + var_name + """Service.update(""" + var_name + """);
		} catch (Exception e) {
			e.printStackTrace();
		}
        return new ResponseEntity<""" + class_name + """>(saved, HttpStatus.OK);
    }
	
	@CrossOrigin
	@RequestMapping(
			value = "/{id}/get",
			method = RequestMethod.GET,
			produces = MediaType.APPLICATION_JSON_VALUE)
	public ResponseEntity<""" + class_name + """> get""" + class_name + """(@PathVariable String id) {
		""" + class_name + """ """ + var_name + """ = """ + var_name + """Service.findOne(Long.parseLong(id));
		
		if(""" + var_name + """ == null){
			return new ResponseEntity<""" + class_name + """>(HttpStatus.NOT_FOUND);
		}

		return new ResponseEntity<""" + class_name + """>(""" + var_name + """,
				HttpStatus.OK);
	}
	
	@CrossOrigin
	@RequestMapping(
			value = "/getAll",
			method = RequestMethod.GET,
			produces = MediaType.APPLICATION_JSON_VALUE)
	public ResponseEntity< ArrayList<""" + class_name + """> > get""" + class_name + """s() {
		ArrayList<""" + class_name + """> """ + var_name + """s = (ArrayList<""" + class_name + """>) """ + var_name + """Service.findAll();
		return new ResponseEntity< ArrayList<""" + class_name + """> >(""" + var_name + """s,
				HttpStatus.OK);
	}
	
	@CrossOrigin
	@RequestMapping(
			value = "/{id}/delete",
			method = RequestMethod.DELETE,
			produces = MediaType.APPLICATION_JSON_VALUE)
	public ResponseEntity<""" + class_name + """> delete""" + class_name + """ById(@PathVariable String id) {
		""" + class_name + """ """ + var_name + """ = """ + var_name + """Service.findOne(Long.parseLong(id));
		
		if(""" + var_name + """ == null){
			return new ResponseEntity<""" + class_name + """>(HttpStatus.NOT_FOUND);
		}

		try {
			""" + var_name + """Service.delete(""" + var_name + """);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return new ResponseEntity<""" + class_name + """>(HttpStatus.OK);
	}
	
	@CrossOrigin
	@RequestMapping(value = "/delete", 
	method = RequestMethod.DELETE,
	consumes = MediaType.APPLICATION_JSON_VALUE,
	produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<""" + class_name + """> delete""" + class_name + """(@RequestBody """ + class_name + """ """ + var_name + """)
    {
		""" + class_name + """ exists = """ + var_name + """Service.findOne(""" + var_name + """.getId());
		
		if(exists == null){
			return new ResponseEntity<""" + class_name + """>(HttpStatus.NOT_FOUND);
		}
        
		try {
			""" + var_name + """Service.delete(""" + var_name + """);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        return new ResponseEntity<""" + class_name + """>(HttpStatus.OK);
    }
	
}
"""
    return content

def main():
    folder = get_folder()
    project_name = get_project_name()
    iterate(folder, project_name)

if __name__ == "__main__":
    main()