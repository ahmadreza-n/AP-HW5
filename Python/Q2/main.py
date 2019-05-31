def render(request, htmlFileName, *args, **keywords):
    print('Html file name:', htmlFileName)
    print('I recieved these datas:')
    [print(arg, end=' ') for arg in args]
    for key in keywords:
        if key is 'title':
            print('your title is:', keywords[key])
        elif key is 'error':
            print('your error code is:', keywords[key])


if __name__ == '__main__':
    render(None, 'test.html', 1, 2, 3, 4, title='testing', error='404')
