<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - GraphX</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>

<body>
    <div class="navbar navbar-inverse navbar-fixed-top" id="app_header">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>

                <a href="/" class="navbar-brand" id="home-page">GraphX</a>

            </div>
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li class="dropdown">
                        <a href="#" id="nav-a-theory" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Теория<span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a id="theory-prim" href="/prima_algorithm_theory">Алгоритм Прима</a></li>
                            <li><a id="theory-daykstra" href="/daykstra_algorithm_theory">Алгоритм Дейкстры</a></li>
                            <li><a id="theory-floyd" href="/floyd_algorithm_theory">Алгоритм Флойда</a></li>
                            <li><a id="theory-kraskal" href="/kraskal_algorithm_theory">Алгоритм Краскала</a></li>
                        </ul>
                    </li>
                    <li class="dropdown">
                        <a href="#" id="nav-a-calc" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Калькулятор<span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a id="calc-prim" href="/prima_algorithm_calc">Алгоритм Прима</a></li>
                            <li><a id="calc-daykstra" href="/daykstra_algorithm_calc">Алгоритм Дейкстры</a></li>
                            <li><a id="calc-floyd" href="/floyd_algorithm_calc">Алгоритм Флойда</a></li>
                            <li><a id="calc-kraskal" href="/kraskal_algorithm_calc">Алгоритм Краскала</a></li>
                        </ul>
                    </li>
                    <li><a href="/about" id="about-page">Об авторах</a></li>
                </ul>
            </div>
        </div>
    </div>

    <div class="container body-content" id="content">
        {{!base}}
    </div>

    <div class="footer">
            <p>&copy; {{ year }} GraphX</p>
            <a href="https://vk.com/college.guap" id="footer_link">Ссылка на группу разработчиков</a>
    </div>

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>