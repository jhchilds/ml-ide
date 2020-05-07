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


    Plotly.animate('classify-visualizer', {
        data: data,
        layout: {}
    }, {
        transition: {
            duration: 500,
            easing: 'cubic-in-out'
        },
        frame: {
            duration: 500
        }
    })


}

function initVisualizer() {
    var data = [
        {
            x: ['c', 'hs', 'java', 'js', 'py', 'swift'],
            y: [0.1,0.1,0.1,0.1,0.1,0.1],
            type: 'bar'
        }
    ];
    Plotly.newPlot('classify-visualizer', data);
}