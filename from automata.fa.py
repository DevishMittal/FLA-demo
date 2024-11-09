from automata.fa.dfa import DFA
import gradio as gr

dfa_q1 = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'1': 'q1', '0': 'q0'},
        'q1': {'1': 'q2', '0': 'q0'},
        'q2': {'1': 'q2', '0': 'q3'},
        'q3': {'0': 'q4', '1': 'q4'},
        'q4': {'0': 'q4', '1': 'q4'}
    },
    initial_state='q0',
    final_states={'q4'}
)

dfa_q2 = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q2', '1': 'q0'},
        'q2': {'0': 'q2', '1': 'q0'}
    },
    initial_state='q0',
    final_states={'q2'}
)

dfa_q3 = DFA(
    states={'q0', 'q1'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q0'},
        'q1': {'a': 'q1', 'b': 'q1'}
    },
    initial_state='q0',
    final_states={'q1'}
)


def validate_dfa(input_string, question):
    if question == "contain '1100'":
        dfa = dfa_q1
    elif question == "Ending '00'":
        dfa = dfa_q2
    elif question == "contain 'a'":
        dfa = dfa_q3
    else:
        return "Invalid Selection"

    current_state = dfa.initial_state
    steps = [f"Start at initial state: {current_state}"]

    for symbol in input_string:
        if symbol not in dfa.input_symbols:
            return f"Invalid input symbol '{symbol}' for DFA."

        next_state = dfa.transitions[current_state].get(symbol)
        steps.append(f"Input: '{symbol}' -> Transition: {current_state} -> {next_state}")
        current_state = next_state

    # Check final state
    if current_state in dfa.final_states:
        steps.append(f"End in final state: {current_state} (Valid String)")
        result = "Valid String"
    else:
        steps.append(f"End in non-final state: {current_state} (Invalid String)")
        result = "Invalid String"

    return "\n".join(steps) + f"\n\nResult: {result}"


iface = gr.Interface(
    fn=validate_dfa,
    inputs=[
        gr.Textbox(label="Enter a string"),
        gr.Radio(["contain '1100'", "Ending '00'", "contain 'a'"], label="Select Question")
    ],
    outputs="text",
    title="DFA String Validator with Step-by-Step Transitions"
)


iface.launch()
