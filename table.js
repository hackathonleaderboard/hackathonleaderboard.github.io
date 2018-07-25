function doSomething(d){
  console.log(d.User)
  window.location.href = "https://devpost.com/" + d.User;
}
var tabulate = function (data,columns) {
    var table = d3.select("#headTable").append('table').attr("class", "container").attr("style","font-family: 'Orbitron'");
      var thead = table.append('thead')
      var tbody = table.append('tbody')
  
      thead.append('tr')
        .selectAll('th')
          .data(columns)
          .enter()
        .append('th')
          .text(function (d) { return d })
  
      var rows = tbody.selectAll('tr')
          .data(data)
          .enter()
        .append('tr')
        .on("click", function(d) { doSomething(d); }) 
  
      var cells = rows.selectAll('td')
          .data(function(row) {
              return columns.map(function (column) {
                  return { column: column, value: row[column] }
            })
        })
        .enter()
      .append('td')
        .text(function (d) { return d.value })
  
    return table;
  }
  
  d3.csv('data.csv',function (data) {
      var columns = ['Rank','User','Score']
    tabulate(data,columns)
  })