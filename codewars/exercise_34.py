def foo(positional, only, /, either, pos, or_='default',
        *, keyword, just, **keywords):
    print(positional, only, either, pos, or_, keyword,
          just, keywords)


foo('a', 'b', 1, 2, 'or_', keyword='keyword', just='just',
    unknown_keyword='unknown_keyword')
