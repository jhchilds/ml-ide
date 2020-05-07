function classifyVisualizer(labeledPredictions) {

    var data = [
        {
            x: ['c', 'hs', 'java', 'js', 'py', 'swift'],
            y: [parseFloat(labeledPredictions.c),
                parseFloat(labeledPredictions.hs),
                parseFloat(labeledPredictions.java),
                parseFloat(labeledPredictions.js),
                parseFloat(labeledPredictions.py),
                parseFloat(labeledPredictions.swift)
            ],
            type: 'bar'
        }
    ];

    Plotly.newPlot('classify-visualizer', data);

}