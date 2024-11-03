"""
goals

Guide the creation of an interactive visualization showing:

Neural network architecture analyzing fractal patterns
Real-time fractal generation based on network outputs
Complex system behavior emergence
Parameter controls for both NN and fractal aspects


Meet Alpha Protocol requirements including:

Strict inline styling
Full interface controls (play/pause, reset, settings)
Mobile-first design (320x480px)
Performance standards (60 FPS, 2s init)


Target a high Webtastic rating through:

Novel visualization approaches
Intuitive parameter controls
Clear educational value
Smooth animations
Creative interactive elements

"""

from data.data import API_KEY

import anthropic
MODEL_NAME = "claude-3-opus-20240229"

client = anthropic.Anthropic(api_key=API_KEY)

def get_completion(prompt: str, system_prompt="", prefill=""):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=4096,
        temperature=0.0,
        system=system_prompt,
        messages=[
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": prefill}
        ]
    )
    return message.content[0].text

######################################## PROMPT ELEMENTS ########################################

##### Prompt element 1: Task context
TASK_CONTEXT = """You are an advanced AI specialized in deep learning, fractal geometry, complex systems, and React-based visualization. You have expertise in:

- Neural network architecture and behavior analysis
- Fractal geometry and self-similarity properties
- React component structures following the Alpha Protocol
- Complex system theory, including emergent behaviors
- Interactive, real-time data visualization techniques

You excel at creating visualizations that:
1. Respect mobile-first design principles (320px width, 480px height)
2. Use plain CSS-in-JS (no libraries like Tailwind)
3. Implement strong error handling
4. Maintain clear component separation and performance efficiency
5. Make complex concepts visually intuitive to users
"""

##### Prompt element 2: Tone context
TONE_CONTEXT = """Maintain a tone that is precise, visually oriented, and implementation-focused. Ensure clarity in complex concepts with an accessible yet technical approach:

Technical Precision:
- Use appropriate mathematical notation where necessary
- Present neural network, fractal, and complex system concepts visually

Implementation Clarity:
- Explain key architectural decisions and optimization techniques
- Detail code components for a single-file setup

Visual Accessibility:
- Use clear visual analogies to explain complex concepts
- Illustrate relationships between neural networks, fractals, and emergent behaviors
"""

##### Prompt element 3: Input data
INPUT_DATA = """<alpha_protocol_constraints>
- Width: 320px; Height: 480px
- Single-file React component
- Only plain CSS in JS styling
- No external libraries
- Built-in React state management
- SVG-based visualization for efficient rendering
- Real-time updates and interactive controls
</alpha_protocol_constraints>

<visualization_requirements>
- Neural network analysis and fractal generation
- Real-time fractal generation based on neural network outputs
- Complex system behavior emergence
- Mobile-responsive design with interactive controls
</visualization_requirements>
"""

##### Prompt element 4: Examples
EXAMPLES = """Here are examples of ideal responses:

<example1>
<neural_network_analysis>
  Neural network parameters influence fractal generation and complex system behavior:
  - Hidden layers control fractal self-similarity
  - Activation functions map fractal parameters
  - Output layers determine emergent patterns

</neural_network_analysis>

<visualization_component>
import React, { useState, useEffect } from 'react';

const NeuralFractalVisualizer = () => {
  const [fractalParams, setFractalParams] = useState({ depth: 4, complexity: 80 });

  const styles = {
    container: { width: '320px', height: '480px', backgroundColor: '#111' }
  };

  return (
    <div style={styles.container}>
      <svg viewBox="0 0 320 480">
        {/* Render fractal here */}
      </svg>
    </div>
  );
};

export default NeuralFractalVisualizer;
</visualization_component>

<complexity_analysis>
  <time_complexity>O(n * log(n)) for fractal rendering where n is recursion depth</time_complexity>
  <optimization_notes>
    - Web Workers for neural computations
    - Virtual DOM for efficient re-renders
  </optimization_notes>
</complexity_analysis>
</example1>

<example2>
<interdisciplinary_connection>
Neural networks influence fractal patterns by modifying recursion depth and complexity. Complex systems display emergent behaviors when NN output layers determine fractal structure, linking machine learning and mathematical recursion.

Key relationships:
1. NN activation functions → Fractal iteration depth
2. Neuron weights → Fractal symmetry
3. System states → Emergent visual patterns

This integration provides a powerful way to visualize complex system theory with dynamic, interactive fractals.
</interdisciplinary_connection>
</example2>
"""

##### Prompt element 5: Task description
TASK_DESCRIPTION = """Develop an interactive visualization system for Neural Fractal Emergence that:

1. Neural Network Framework:
   - Analyzes fractal patterns based on NN outputs
   - Displays parameter influence on fractal structure

2. Visual Implementation:
   - Follows Alpha Protocol constraints
   - Provides real-time controls for NN and fractal parameters
   - Mobile-responsive with SVG rendering for efficiency

3. Documentation:
   - Explains neural and fractal integration
   - Describes implementation choices
   - Includes user guidelines

Your response should:
- Begin with theoretical foundations
- Progress to practical implementation with code examples
- Include performance optimization and error-handling strategies
"""

##### Prompt element 6: Immediate task
IMMEDIATE_TASK = """Using the framework provided, create a comprehensive visualization for Neural Fractal Emergence. Emphasize the integration of neural network outputs with fractal patterns, parameter controls, and real-time interaction, adhering to Alpha Protocol specifications."""

##### Prompt element 7: Precognition
PRECOGNITION = """Before responding, perform the following analyses:

1. Neural Network Analysis:
   - Identify NN parameters affecting fractal output
   - Define fractal generation based on NN states

2. Technical Planning:
   - Confirm Alpha Protocol compliance
   - Plan single-file component structure
   - Design state management with parameter controls

3. Visualization Strategy:
   - Connect NN layers to fractal iterations
   - Map NN output to fractal depth and symmetry

4. Implementation Planning:
   - Consider optimization strategies
   - Plan for error boundaries and responsive layout

Only proceed with these analyses in mind."""

##### Prompt element 8: Output formatting
OUTPUT_FORMATTING = """Format your response as follows:

<neural_network_framework>
  <nn_parameters>
    Define neural network parameters influencing fractal generation
  </nn_parameters>
  
  <fractal_patterns>
    Fractal generation algorithms and self-similarity relationships
  </fractal_patterns>
</neural_network_framework>

<implementation>
  <component_architecture>
    React component structure and parameter relationships
  </component_architecture>
  
  <visualization_code>
    Complete code implementation following Alpha Protocol
  </visualization_code>
  
  <error_handling>
    Comprehensive error management strategies
  </error_handling>
</implementation>

<analysis>
  <performance>
    Complexity analysis and optimizations
  </performance>
  
  <limitations>
    Protocol constraints and alternatives
  </limitations>
</analysis>
"""

##### Prompt element 9: Prefill
PREFILL = ""

######################################## COMBINE ELEMENTS ########################################

PROMPT = ""

if TASK_CONTEXT:
    PROMPT += f"""{TASK_CONTEXT}"""

if TONE_CONTEXT:
    PROMPT += f"""\n\n{TONE_CONTEXT}"""

if INPUT_DATA:
    PROMPT += f"""\n\n{INPUT_DATA}"""

if EXAMPLES:
    PROMPT += f"""\n\n{EXAMPLES}"""

if TASK_DESCRIPTION:
    PROMPT += f"""\n\n{TASK_DESCRIPTION}"""

if IMMEDIATE_TASK:
    PROMPT += f"""\n\n{IMMEDIATE_TASK}"""

if PRECOGNITION:
    PROMPT += f"""\n\n{PRECOGNITION}"""

if OUTPUT_FORMATTING:
    PROMPT += f"""\n\n{OUTPUT_FORMATTING}"""

# Print full prompt
print("--------------------------- Full prompt with variable substitutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT, prefill=PREFILL))
