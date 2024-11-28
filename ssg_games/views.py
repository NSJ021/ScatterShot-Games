"""
This module contains the views for the game application.

Views:
    Games: Renders a list of all the games in the database.
    game_detail: Displays an individual game entry.
"""
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse
from ssg_games.models import Game, Comment


from .forms import CommentForm
# Import Paginator for paginating the list of games

# Create your views here.


def games(request):
    """
    Renders a list of all the games in the database.

    """
    game_list = Game.objects.order_by(
        'game_title')  # Fetch all game entries ordering by game_title
    # Paginate the queryset by 4 games per page
    paginator = Paginator(game_list, 4)
    page = request.GET.get('page')  # Get the current page number
    # Get the games for the current page
    paged_games = paginator.get_page(page)

    context = {
        'games': paged_games  # Pass the paginated games to the template
    }

    return render(request, 'ssg_games/games.html', context)


def game_detail(request, slug):
    """
    Displays the details of an individual game entry.
    """
    queryset = Game.objects.all()  # Fetch all game entries
    # Fetch the game with the given slug
    game = get_object_or_404(queryset, slug=slug)
    comments = game.game_comments.all().order_by("-created_on")
    comment_count = game.game_comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.game = game
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()
    return render(
        request,
        "ssg_games/game_detail.html",
        {
            "game": game,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },

    )


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for editing.
    """
    if request.method == "POST":

        queryset = Game.objects.all()
        game = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.game = game
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('game_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment
    """
    # queryset = Game.objects.all()
    # game = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('game_detail', args=[slug]))
