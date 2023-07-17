from flask import Blueprint, make_response, jsonify, request
from mazeCreator import mazeCreator
from putter import putter

maze = Blueprint('maze', __name__)


@maze.route('/')
def index():
    return make_response(
        jsonify({
            'message': 'maze'
        }),
        200
    )


@maze.route('/create')
def create_maze():
    try:
        row = int(request.args.get('row'))
        col = int(request.args.get('col'))
    except TypeError:
        return make_response(
            jsonify({
                'message': 'maze',
                'error': 'row and col must be int'
            }),
            400
        )
    if row % 2 == 0 or col % 2 == 0:
        return make_response(
            jsonify({
                'message': 'maze',
                'error': 'row and col must be odd'
            }),
            400
        )
    if row < 5 or col < 5:
        return make_response(
            jsonify({
                'message': 'maze',
                'error': 'row and col must be greater than 5'
            }),
            400
        )
    try:
        _maze = mazeCreator(row - 2, col - 2)
    except RecursionError:
        return make_response(
            jsonify({
                'message': 'maze',
                'error': 'row and col is too large'
            }),
            400
        )
    _maze, start_pos, end_pos = putter(_maze, col, row)
    return make_response(
        jsonify({
            'message': 'maze',
            'maze': _maze,
            'start_pos': start_pos,
            'end_pos': end_pos,
            'row': row,
            'col': col
        }),
        200
    )
