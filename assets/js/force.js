var width = 500,
    height = 200;

var color = d3.scale.category20();

var force = d3.layout.force()
    .charge(-120)
    .linkDistance(30)
    .size([width, height]);

var svg = d3.select("#chart").append("svg")
    .attr("width", width)
    .attr("height", height);

d3.json("assets/data/nodes.json", function(json) {

// Calcular la cantidad de links de cada nodo
// Ver node.attr("r")
  var links = [];
  json.links.forEach(function(l) {
    if (typeof(links[l.target]) == "undefined") links[l.target] = 0;
    if (typeof(links[l.source]) == "undefined") links[l.source] = 0;

    links[l.target]++;
    links[l.source]++;
  });

  force
      .nodes(json.nodes)
      .links(json.links)
      .start();

  var link = svg.selectAll("line.link")
      .data(json.links)
    .enter().append("line")
      .attr("class", "link");

  var node = svg.selectAll("circle.node")
      .data(json.nodes)
    .enter().append("circle")
      .attr("class", "node")
      .attr("r", function(d) { return links[d.index]; })
      .style("fill", function(d) { return color(d.weight); })
      .call(force.drag);

  node.append("title")
      .text(function(d) { return d.name; });

  force.on("tick", function() {
    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node.attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
  });
});
