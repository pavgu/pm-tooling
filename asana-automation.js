function logProductInfo() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet();
  sheet = sheet.getSheetByName("Clarity Milestones");
  var data = sheet.getDataRange().getValues();
  var appMilestones = ['Application Discovery Complete','Application Initial Design Complete','Start work in Landing Zone','Application Development Fully Complete','Application Go Live','In scope legacy CI decommissioned'];
  var header = "Name, Type, Due Date, Wave (DB), Line of Business (DB), Workstream (DB), Application Name (DB)\n";
  var output = header;
  var folderId = DriveApp.createFolder('Asana for DB').getId();
  for (var i = 1; i <= 25; i++) {
    var appName = data[i][4];
    var wave = data[i][5];
    var lob = data[i][6];
    var workstream = data[i][7];
    for (var j = 0; j<= 5; j++) {
      var d = new Date(data[i][11+j]);
      var dateFormatted = (d.getMonth() + 1) + "/" + d.getDate() + "/" + d.getFullYear(); 
      var csvEntry = appMilestones[j] + "," + "Milestone" + "," + dateFormatted + "," + wave + "," + lob + "," + workstream + "," + appName + "\n";
      output+=csvEntry;
    }
    var file = DriveApp.getFolderById(folderId).createFile(appName + ".csv", output)
    output = header;  
  }
}
